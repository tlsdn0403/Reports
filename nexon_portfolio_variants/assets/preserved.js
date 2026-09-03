const CANVA = "assets/canva/";
const MEDIA = "assets/media/";

const variants = {
  signal: { number: "01", name: "CANVA CONTINUITY", note: "기존 Canva와 가장 자연스럽게 이어지는 안" },
  blueprint: { number: "02", name: "SYSTEM BLUEPRINT", note: "네트워크 구조와 상태 흐름을 강조한 안" },
  cinematic: { number: "03", name: "PLAYABLE SCENE", note: "게임 화면과 결과를 크게 보여주는 안" },
  editorial: { number: "04", name: "CODE REVIEW", note: "문제와 판단 근거를 읽기 좋게 정리한 안" },
  board: { number: "05", name: "FLICK BOARD", note: "FlickDom의 보드게임 개성을 살린 안" },
};

const files = {
  signal: "candidate-01.html",
  blueprint: "candidate-02.html",
  cinematic: "candidate-03.html",
  editorial: "candidate-04.html",
  board: "candidate-05.html",
};

const originalAlt = {
  1: "GAME CLIENT PORTFOLIO 표지. 박신우 Client Programmer, 이메일과 GitHub.",
  2: "Tech Stack. C++, Unreal Engine, Unity, GitHub, Visual Studio 활용 역량.",
  3: "Project Index. 감염 죽음의 도시, FlickDom, Bubble Fighter IP 프로젝트.",
  4: "Project 01 감염 죽음의 도시 소개. UE5 C++ 협동 TPS 졸업작품.",
  5: "좀비 신체 분리 구조 설계와 두 결과 영상.",
  6: "Truck Interaction. 아이템 적재, 기관총 사용, 트럭 운전 영상 교체 위치.",
  7: "Project 02 FlickDom 소개. Unity C# WebGL, Network Turn Board 담당.",
  8: "읽어주셔서 감사합니다. 박신우 게임 클라이언트 프로그래머.",
};

function originalSlide(page) {
  const videos = page === 5 ? `
    <video class="canva-video dismemberment" src="${CANVA}zombie-dismemberment.mp4" autoplay muted loop playsinline controls aria-label="좀비 신체분리 결과 영상"></video>
    <video class="canva-video crawling" src="${CANVA}zombie-crawling.mp4" autoplay muted loop playsinline controls aria-label="좀비 다리 절단 후 기어가기 상태 전환 영상"></video>` : "";
  return `<section class="deck-slide original-slide" aria-label="기존 Canva ${page}페이지">
    <img src="${CANVA}page-${String(page).padStart(2, "0")}.png" alt="${originalAlt[page]}">
    ${videos}
  </section>`;
}

function githubIcon() {
  return `<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 .7a11.5 11.5 0 0 0-3.64 22.42c.58.11.79-.25.79-.56v-2.02c-3.22.7-3.9-1.37-3.9-1.37-.53-1.34-1.29-1.7-1.29-1.7-1.05-.72.08-.7.08-.7 1.17.08 1.78 1.2 1.78 1.2 1.04 1.78 2.72 1.27 3.38.97.1-.75.4-1.27.74-1.56-2.57-.29-5.27-1.28-5.27-5.68 0-1.25.45-2.28 1.19-3.08-.12-.29-.52-1.46.11-3.04 0 0 .97-.31 3.16 1.18a10.96 10.96 0 0 1 5.75 0c2.2-1.49 3.16-1.18 3.16-1.18.63 1.58.23 2.75.11 3.04.74.8 1.19 1.83 1.19 3.08 0 4.41-2.71 5.38-5.29 5.67.42.36.79 1.06.79 2.14v3.18c0 .31.21.68.8.56A11.5 11.5 0 0 0 12 .7Z"/></svg>`;
}

function youtubeIcon() {
  return `<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M23.5 6.2a3 3 0 0 0-2.1-2.12C19.55 3.58 12 3.58 12 3.58s-7.55 0-9.4.5A3 3 0 0 0 .5 6.2 31.2 31.2 0 0 0 0 12a31.2 31.2 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.12c1.85.5 9.4.5 9.4.5s7.55 0 9.4-.5a3 3 0 0 0 2.1-2.12A31.2 31.2 0 0 0 24 12a31.2 31.2 0 0 0-.5-5.8ZM9.6 15.6V8.4l6.27 3.6-6.27 3.6Z"/></svg>`;
}

function projectLinks(github, youtube) {
  return `<div class="project-links" aria-label="프로젝트 외부 링크">
    <a class="github" href="${github}" target="_blank" rel="noreferrer" aria-label="GitHub 저장소 열기" title="GitHub 저장소">${githubIcon()}<span>GITHUB</span></a>
    <a class="youtube" href="${youtube}" target="_blank" rel="noreferrer" aria-label="YouTube 영상 열기" title="YouTube 영상">${youtubeIcon()}<span>VIDEO</span></a>
  </div>`;
}

function projectIntro({ number, projectNo, title, subtitle, image, imageAlt, github, youtube, fields }) {
  return `<section class="deck-slide project-intro" aria-label="${title} 프로젝트 소개">
    <div class="intro-top">
      <div><p>${projectNo} / PROJECT INTRO</p><h2>${title}<small>${subtitle}</small></h2></div>
      ${projectLinks(github, youtube)}
    </div>
    <div class="intro-rule"></div>
    <div class="intro-layout">
      <figure class="intro-image"><img src="${MEDIA + image}" alt="${imageAlt}"><figcaption>${title} · GAME PLAY</figcaption></figure>
      <dl class="project-facts">
        ${fields.map(([label, value]) => `<div><dt>${label}</dt><dd>${value}</dd></div>`).join("")}
      </dl>
    </div>
    <span class="intro-page-number">${number}</span>
  </section>`;
}

function infectionIntro() {
  return projectIntro({
    number: "04",
    projectNo: "PROJECT 01",
    title: "감염: 죽음의 도시",
    subtitle: "INFECTION: CITY OF DEATH",
    image: "deck_image1.png",
    imageAlt: "감염 죽음의 도시 프로젝트 로고",
    github: "https://github.com/tlsdn0403/SYJ",
    youtube: "https://www.youtube.com/watch?v=gjeotDi06Fc&t=170s",
    fields: [
      ["프로젝트 이름", "감염: 죽음의 도시"],
      ["장르", "Co-op TPS · Zombie Survival"],
      ["설명", "UE5/C++ 기반 4인 협동 TPS 졸업작품. 플레이어가 팀을 이루어 좀비를 상대하고 생존 목표를 수행합니다."],
      ["개발 인원", "4명 · Team Project"],
      ["담당 역할", "Client Programmer · 좀비 신체 분리·기어가기 전환·Truck Interaction"],
      ["개발 언어", "C++"],
      ["사용 IDE", "Unreal Engine 5 · Visual Studio 2022 · Git"],
      ["AI 모델", "해당 없음"],
      ["제작 기간", "2025.12.20 - 2026.07.08"],
    ],
  });
}

function flickdomIntro() {
  return projectIntro({
    number: "12",
    projectNo: "PROJECT 02",
    title: "FlickDom",
    subtitle: "AI VIBE CODING",
    image: "flickdom_FlickDom.png",
    imageAlt: "FlickDom 메인 화면",
    github: "https://github.com/AACHANJINAA/FlickDom",
    youtube: "https://www.youtube.com/watch?v=ddM9ggItGwQ",
    fields: [
      ["프로젝트 이름", "FlickDom (AI VIBE CODING)"],
      ["장르", "1 VS 1 전략 플릭 보드게임"],
      ["설명", "디스크를 튕겨 5×5 보드 칸을 점령하고, 카드 패턴과 보드 상태가 일치하면 점수를 얻는 물리 기반 게임입니다."],
      ["개발 인원", "3명 · Team Project"],
      ["담당 역할", "Client / Server / Build · Board·Card Pattern·Stage·Turn FSM·Network 수정·WebGL"],
      ["개발 언어", "C#"],
      ["사용 IDE", "Unity 6 Editor · Visual Studio · VS Code · Git"],
      ["AI 모델", "GPT-5 Codex · Unity MCP / Team: Blender·Substance MCP · VARCO AI Sound"],
      ["제작 기간", "2026.07.01 - 2026.08.10"],
    ],
  });
}

function pageHead(number, eyebrow, title, copy = "") {
  return `<header class="page-head">
    <div><p class="eyebrow">${eyebrow}</p><h2>${title}</h2>${copy ? `<p class="page-copy">${copy}</p>` : ""}</div>
    <span class="page-number">${number}</span>
  </header>`;
}

function gameSystem() {
  return `<section class="deck-slide custom-slide game-system">
    ${pageHead("13", "PROJECT 02 · FLICKDOM", "게임 시스템", "디스크를 튕겨 보드 칸을 점령하고 카드 패턴을 완성해 점수를 겨루는 1대1 물리 보드게임입니다.")}
    <div class="feature-grid">
      <figure><img src="${MEDIA}flickdom_intro_2-1.png" alt="카드 패턴과 보드 화면"><figcaption><strong>목표</strong><span>3개의 디스크로 칸을 점령하고 카드 패턴을 완성합니다.</span></figcaption></figure>
      <figure><img src="${MEDIA}flickdom_intro_2-2.png" alt="디스크 조작 화면"><figcaption><strong>조작</strong><span>드래그 방향과 힘으로 디스크를 발사해 다음 턴을 설계합니다.</span></figcaption></figure>
      <figure><img src="${MEDIA}flickdom_intro_3-1.png" alt="FlickDom 멀티플레이 로비"><figcaption><strong>멀티플레이</strong><span>Host가 생성한 Join Code를 공유해 Client가 같은 방에 접속합니다.</span></figcaption></figure>
    </div>
    <div class="rule-strip"><span>3 STAGES</span><span>9 CARDS</span><span>5 × 5 BOARD</span><span>1 VS 1</span></div>
  </section>`;
}

function multiplayerFlow() {
  return `<section class="deck-slide custom-slide multiplayer-flow">
    ${pageHead("14", "FLICKDOM · MULTIPLAYER", "같은 방에 들어오기까지", "친구 포트폴리오의 접속 흐름을 유지하고, 실제 프로젝트 화면으로 단계별 상태를 보여줍니다.")}
    <div class="flow-visuals">
      <figure><img src="${MEDIA}flickdom_intro_3-2.png" alt="멀티플레이 시작 전 로비"><span>01</span><figcaption>Host / Client 역할 선택</figcaption></figure>
      <figure><img src="${MEDIA}flickdom_intro_3-4.png" alt="Join Code 화면"><span>02</span><figcaption>Host가 최신 Join Code 공유</figcaption></figure>
      <figure><img src="${MEDIA}flickdom_intro_3-3.png" alt="Client 접속 상태 표시"><span>03</span><figcaption>Client 접속과 Players 상태 확인</figcaption></figure>
      <figure><img src="${MEDIA}flickdom_intro_2-2.png" alt="FlickDom 플레이 화면"><span>04</span><figcaption>동일한 보드 상태로 게임 시작</figcaption></figure>
    </div>
    <div class="flow-line" aria-label="멀티플레이 접속 순서"><strong>CREATE ROOM</strong><i>→</i><strong>SHARE CODE</strong><i>→</i><strong>JOIN</strong><i>→</i><strong>SYNC STATE</strong></div>
  </section>`;
}

function ownership() {
  return `<section class="deck-slide custom-slide ownership">
    ${pageHead("15", "FLICKDOM · TEAM OWNERSHIP", "함께 만든 결과에서<br>내 구현 범위를 분리했습니다.")}
    <div class="role-table">
      <article><div class="member"><strong>임찬진</strong><span>PLANNING / CLIENT / SERVER</span></div><p>게임 규칙·카드·점수·승리 조건, Drag/Flick, Trajectory, 사운드, 초기 Host/Client 동기화 기반.</p></article>
      <article class="mine"><div class="member"><strong>박신우</strong><span>CLIENT / SERVER / BUILD · MY SCOPE</span></div><p>5×5 보드 점령, Cell 선택·배치 후보, Card Pattern Matching, Stage, 턴 FSM, 멀티 상태 전환, Network 구조 수정, WebGL 배포·브라우저 검증.</p></article>
      <article><div class="member"><strong>황인성</strong><span>MATERIAL / SHADER / 3D·2D ART</span></div><p>Board·Disk·Star 리소스, Scene Prefab, Material·Shader, Gameplay HUD, Rule Screen, Victory UI.</p></article>
    </div>
    <p class="role-note">초기 네트워크 기반 전체를 개인 작업으로 표현하지 않고, 그 위에서 직접 맡은 턴 흐름·상태 전환·보드 로직·WebGL 범위를 설명합니다.</p>
  </section>`;
}

function technicalCase() {
  return `<section class="deck-slide custom-slide technical-case">
    ${pageHead("16", "FLICKDOM · TECHNICAL CASE", "Client는 요청하고,<br>Host가 결과를 확정합니다.")}
    <div class="technical-layout">
      <div class="problem-copy">
        <article><span>PROBLEM</span><h3>즉시 반응과 일관된 물리 결과가 모두 필요했습니다.</h3><p>P2가 Host Transform만 기다리면 입력 반응이 늦고, Client 물리를 그대로 믿으면 두 화면의 결과가 달라질 수 있었습니다.</p></article>
        <article><span>SOLUTION</span><h3>입력 예측과 최종 판정을 분리했습니다.</h3><p>Client는 입력 직후 로컬 예측을 시작하고 FlickRequest를 전송합니다. Host가 턴·소유자·말 ID·힘 범위를 검증한 뒤 PhysicsSettled Snapshot으로 결과를 확정합니다.</p></article>
      </div>
      <div class="network-map" role="img" aria-label="Client 예측, Host 검증, Snapshot 보정 흐름">
        <div><small>P2 CLIENT</small><strong>Predict</strong><span>direction · power</span></div>
        <i>REQUEST →</i>
        <div class="host"><small>HOST</small><strong>Validate</strong><span>turn · owner · piece</span></div>
        <i>SNAPSHOT →</i>
        <div><small>P2 CLIENT</small><strong>Reconcile</strong><span>PhysicsSettled</span></div>
      </div>
    </div>
    <div class="state-strip"><span><b>BoardState</b>5×5 owner grid</span><span><b>ScoreState</b>score · winner</span><span><b>CardState</b>stage · seed · claimed</span><span><b>Stale Guard</b>old state reject</span></div>
  </section>`;
}

function aiWorkflow() {
  return `<section class="deck-slide custom-slide ai-workflow">
    ${pageHead("17", "FLICKDOM · AI/MCP WORKFLOW", "AI 제안은 빠르게,<br>최종 판단은 실행 결과로.")}
    <div class="ai-layout">
      <div class="ai-media">
        <figure><img src="${MEDIA}flickdom_Project_MD.png" alt="MD 기반 프로젝트 문서"><figcaption>01 · CONTEXT / 문서로 작업 경계 전달</figcaption></figure>
        <figure><img src="${MEDIA}flickdom_Unity_MCP.png" alt="Unity MCP 작업 화면"><figcaption>02 · ASSIST / Editor 확인 보조</figcaption></figure>
        <figure><img src="${MEDIA}flickdom_Varco_EffectSound.png" alt="VARCO AI Sound 작업 화면"><figcaption>TEAM TOOL / AI SOUND</figcaption></figure>
      </div>
      <div class="ai-copy">
        <article><span>CONTEXT</span><h3>Architecture · Gameplay Rules · Server Plan · WebGL Build</h3><p>AI가 현재 구조와 제약을 먼저 읽도록 MD 문서로 맥락을 정리했습니다.</p></article>
        <article><span>VERIFY</span><h3>코드·로그·실행 화면으로 재검증</h3><p>네트워크 판정과 빌드 결과는 AI 답변이 아니라 실제 실행 흐름으로 확인했습니다.</p></article>
        <p class="team-note">팀 제작 과정에서는 Blender/Substance MCP와 VARCO AI Sound도 리소스·사운드 제작에 활용했습니다.</p>
      </div>
    </div>
  </section>`;
}

function topbar(theme, config) {
  const links = Object.entries(variants).map(([key, value]) => `<a href="${files[key]}" ${key === theme ? 'aria-current="page"' : ""} title="${value.name}">${value.number}</a>`).join("");
  return `<header class="topbar"><a href="index.html" class="back">← 5안 비교</a><p><b>${config.name}</b><span>${config.note}</span></p><nav aria-label="FlickDom 디자인 후보 전환">${links}</nav><button type="button" id="print">PDF 저장</button></header>`;
}

const theme = document.body.dataset.theme || "signal";
const config = variants[theme];
document.title = `박신우 포트폴리오 · ${config.name}`;
document.querySelector("#app").innerHTML = `${topbar(theme, config)}<main class="deck">
  ${[1, 2, 3].map(originalSlide).join("")}
  ${infectionIntro()}
  ${[5, 6].map(originalSlide).join("")}
  ${flickdomIntro()}
  ${gameSystem()}${multiplayerFlow()}${ownership()}${technicalCase()}${aiWorkflow()}
  ${originalSlide(8)}
</main>`;
document.querySelector("#print").addEventListener("click", () => window.print());
