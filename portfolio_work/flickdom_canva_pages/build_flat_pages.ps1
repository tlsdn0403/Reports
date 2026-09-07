Add-Type -AssemblyName System.Drawing

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$assets = Join-Path $root "assets"
$out = Join-Path $root "out"
New-Item -ItemType Directory -Force -Path $out | Out-Null

function New-Brush($hex) {
    return New-Object System.Drawing.SolidBrush ([System.Drawing.ColorTranslator]::FromHtml($hex))
}

function New-Pen($hex, $width = 1) {
    return New-Object System.Drawing.Pen ([System.Drawing.ColorTranslator]::FromHtml($hex)), $width
}

function RoundedPath($x, $y, $w, $h, $r) {
    $p = New-Object System.Drawing.Drawing2D.GraphicsPath
    $d = $r * 2
    $p.AddArc($x, $y, $d, $d, 180, 90)
    $p.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
    $p.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
    $p.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
    $p.CloseFigure()
    return $p
}

function Draw-RoundedRect($g, $x, $y, $w, $h, $r, $fill, $stroke = $null, $strokeWidth = 1) {
    $p = RoundedPath $x $y $w $h $r
    $g.FillPath((New-Brush $fill), $p)
    if ($stroke) {
        $pen = New-Object System.Drawing.Pen ([System.Drawing.ColorTranslator]::FromHtml($stroke)), $strokeWidth
        $g.DrawPath($pen, $p)
        $pen.Dispose()
    }
    $p.Dispose()
}

function Draw-Text($g, $text, $x, $y, $w, $h, $size, $weight, $color, $align = "Near") {
    $style = [System.Drawing.FontStyle]::Regular
    if ($weight -eq "bold") { $style = [System.Drawing.FontStyle]::Bold }
    $font = New-Object System.Drawing.Font "Malgun Gothic", $size, $style, [System.Drawing.GraphicsUnit]::Pixel
    $brush = New-Brush $color
    $fmt = New-Object System.Drawing.StringFormat
    $fmt.Alignment = [System.Drawing.StringAlignment]::$align
    $fmt.LineAlignment = [System.Drawing.StringAlignment]::Near
    $fmt.Trimming = [System.Drawing.StringTrimming]::EllipsisWord
    $fmt.FormatFlags = 0
    $rect = New-Object System.Drawing.RectangleF $x, $y, $w, $h
    $g.DrawString($text, $font, $brush, $rect, $fmt)
    $fmt.Dispose(); $brush.Dispose(); $font.Dispose()
}

function Draw-CoverImage($g, $path, $x, $y, $w, $h, $radius = 8) {
    $img = [System.Drawing.Image]::FromFile($path)
    $srcRatio = $img.Width / $img.Height
    $dstRatio = $w / $h
    if ($srcRatio -gt $dstRatio) {
        $srcH = $img.Height
        $srcW = [int]($srcH * $dstRatio)
        $srcX = [int](($img.Width - $srcW) / 2)
        $srcY = 0
    } else {
        $srcW = $img.Width
        $srcH = [int]($srcW / $dstRatio)
        $srcX = 0
        $srcY = [int](($img.Height - $srcH) / 2)
    }
    $state = $g.Save()
    $clip = RoundedPath $x $y $w $h $radius
    $g.SetClip($clip)
    $dest = New-Object System.Drawing.Rectangle $x, $y, $w, $h
    $src = New-Object System.Drawing.Rectangle $srcX, $srcY, $srcW, $srcH
    $g.DrawImage($img, $dest, $src, [System.Drawing.GraphicsUnit]::Pixel)
    $g.Restore($state)
    $clip.Dispose()
    $img.Dispose()
    Draw-RoundedRect $g $x $y $w $h $radius "#00000000" "#dbe3ee" 1
}

function Draw-PageHeader($g, $eyebrow, $title, $sub = "") {
    Draw-Text $g $eyebrow 28 22 420 24 17 "bold" "#6254f3"
    Draw-Text $g $title 28 48 520 58 54 "bold" "#6254f3"
    if ($sub) { Draw-Text $g $sub 286 62 330 34 28 "bold" "#6254f3" }
    $pen = New-Object System.Drawing.Pen ([System.Drawing.Color]::FromArgb(31,41,55)), 3
    $g.DrawLine($pen, 28, 112, 1332, 112)
    $pen.Dispose()
}

function New-PageBitmap($path) {
    $bmp = New-Object System.Drawing.Bitmap 1366, 768
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit
    $g.Clear([System.Drawing.ColorTranslator]::FromHtml("#f8fafc"))
    & $script:drawContent $g
    $bmp.Save($path, [System.Drawing.Imaging.ImageFormat]::Png)
    $g.Dispose(); $bmp.Dispose()
}

$script:drawContent = {
    param($g)
    Draw-PageHeader $g "FlickDom / PAGE 01" "FlickDom" "(AI VIBE CODING)"
    Draw-RoundedRect $g 1118 24 112 32 16 "#ffffff" "#cbd5e1" 1
    Draw-Text $g "GITHUB" 1141 32 76 18 14 "bold" "#111827"
    Draw-RoundedRect $g 1242 24 92 32 16 "#ffffff" "#cbd5e1" 1
    Draw-Text $g "VIDEO" 1264 32 58 18 14 "bold" "#dc2626"
    Draw-RoundedRect $g 1242 64 92 32 8 "#6254f3"
    Draw-Text $g "Team Project" 1253 72 75 18 12 "bold" "#ffffff"

    Draw-CoverImage $g (Join-Path $assets "flickdom-cover.png") 28 156 744 416 8
    Draw-RoundedRect $g 796 132 536 514 12 "#ffffff" "#d7dee8" 1
    $pen = New-Object System.Drawing.Pen ([System.Drawing.ColorTranslator]::FromHtml("#0ea5e9")), 4
    $g.DrawLine($pen, 944, 178, 944, 606)
    $pen.Dispose()

    $rows = @(
        @("프로젝트`n이름", "FlickDom (AI VIBE CODING)"),
        @("장르", "1 VS 1 전략 플릭 보드게임"),
        @("설명", "디스크를 튕겨 보드 칸을 차지하고 카드 패턴을 완성해 점수를 겨루는 물리 기반 파티 게임"),
        @("개발 인원", "팀 프로젝트"),
        @("담당 역할", "Unity MCP 기반 구현 반복, 멀티플레이 흐름, UI/UX, 사운드 제작 및 적용"),
        @("개발 언어", "C#"),
        @("사용 IDE", "Unity 6 Editor, VS Code, Blender, Substance 3D Designer"),
        @("AI 모델", "GPT-5 Codex, Unity MCP, Blender MCP, Substance MCP, VARCO AI Sound"),
        @("제작 기간", "2026.07.01 ~ 2026.08.10")
    )
    $y = 166
    foreach ($row in $rows) {
        Draw-Text $g $row[0] 835 $y 86 48 17 "bold" "#111827" "Far"
        Draw-Text $g $row[1] 982 $y 306 52 17 "bold" "#111827"
        $y += 48
    }
    Draw-Text $g "GitHub  github.com/AACHANJINAA/FlickDom" 28 684 600 24 16 "bold" "#334155"
    Draw-Text $g "Video  youtube.com/watch?v=ddM9ggItGwQ" 28 712 620 24 16 "bold" "#334155"
}
New-PageBitmap (Join-Path $out "flickdom-page-01.png")

$script:drawContent = {
    param($g)
    Draw-PageHeader $g "FlickDom / PAGE 02" "게임 시스템"
    $cards = @(
        @("flickdom-goal.png", "목표", "3개의 디스크로 보드 칸을 점령하고 카드 패턴을 완성합니다."),
        @("flickdom-control.png", "조작", "디스크를 선택한 뒤 드래그 방향과 힘으로 발사해 다음 턴 전략을 만듭니다."),
        @("flickdom-multi.png", "멀티플레이", "Host가 방을 생성하고 Join Code를 공유하면 Client가 접속합니다.")
    )
    $x = 28
    foreach ($card in $cards) {
        Draw-RoundedRect $g $x 132 420 370 8 "#ffffff" "#d7dee8" 1
        Draw-CoverImage $g (Join-Path $assets $card[0]) $x 132 420 228 8
        Draw-Text $g $card[1] ($x + 18) 380 170 28 21 "bold" "#6254f3"
        Draw-Text $g $card[2] ($x + 18) 418 370 54 15 "bold" "#111827"
        $x += 438
    }

    $flows = @(
        @("flickdom-multi.png", "시작 전 준비", "Host / Client 역할 확인"),
        @("flickdom-multi.png", "Join Code 입력", "초대를 코드로 교환 및 접속"),
        @("flickdom-goal.png", "상태 표시", "점수 및 역할 상태 확인"),
        @("flickdom-control.png", "결과 전파", "최신 보드 공유 후 시작")
    )
    $x = 28
    foreach ($flow in $flows) {
        Draw-RoundedRect $g $x 516 310 86 8 "#ffffff" "#d7dee8" 1
        Draw-CoverImage $g (Join-Path $assets $flow[0]) ($x + 10) 534 82 50 4
        Draw-Text $g $flow[1] ($x + 108) 532 180 18 14 "bold" "#6254f3"
        Draw-Text $g $flow[2] ($x + 108) 554 180 28 12 "bold" "#111827"
        $x += 328
    }

    Draw-RoundedRect $g 28 622 1304 80 8 "#f1f8ff" "#dbeafe" 1
    $pen = New-Object System.Drawing.Pen ([System.Drawing.ColorTranslator]::FromHtml("#0ea5e9")), 8
    $g.DrawLine($pen, 34, 630, 34, 694)
    $pen.Dispose()
    Draw-Text $g "AI/MCP 활용으로 이어지는 제작`n과정" 56 640 270 46 22 "bold" "#0ea5e9"
    Draw-Text $g "Unity MCP, Blender MCP, Substance MCP와 AI 사운드 제작 흐름을 함께 활용해 리소스 정리와 구현 반복 속도를 높였습니다." 360 642 900 42 17 "bold" "#111827"
}
New-PageBitmap (Join-Path $out "flickdom-page-02.png")
