const MEDIA = "assets/media/";

const variants = {
  signal: {
    number: "01",
    name: "NEXON SIGNAL",
    summary: "채용담당자가 핵심 역량과 대표 문제 해결을 가장 빠르게 읽는 구성",
    heroLabel: "GAME CLIENT PROGRAMMER",
    heroTitle: "플레이 감각을\n신뢰할 수 있는 코드로",
    heroCopy: "C++과 C#으로 상호작용을 구현하고, 멀티플레이 상태를 검증 가능한 구조로 정리하는 게임 클라이언트 프로그래머 박신우입니다.",
    heroMedia: "deck_image11.jpeg",
    order: ["profile", "projects", "infection", "flickdom", "network", "ownership", "ai", "contact"],
  },
  blueprint: {
    number: "02",
    name: "SYSTEM BLUEPRINT",
    summary: "Host 권한, Snapshot, FSM을 중심에 둔 기술 면접 대응형",
    heroLabel: "CLIENT / NETWORK / STATE",
    heroTitle: "상태의 소유권을 정하고\n끝까지 동기화합니다",
    heroCopy: "입력은 즉시 반응하고 결과는 일관되어야 합니다. FlickDom에서 턴 FSM과 보드·카드·점수 상태 경계를 다듬고 WebGL까지 검증했습니다.",
    heroMedia: "flickdom_intro_2-2.png",
    order: ["profile", "flickdom", "network", "ownership", "infection", "projects", "ai", "contact"],
  },
  cinematic: {
    number: "03",
    name: "PLAYABLE SCENE",
    summary: "큰 게임 화면과 짧은 문장으로 결과물을 먼저 보여주는 시네마틱형",
    heroLabel: "FROM PLAY TO SYSTEM",
    heroTitle: "움직이는 장면 뒤의\n규칙을 구현합니다",
    heroCopy: "좀비 피격 반응부터 1대1 물리 보드게임의 네트워크 흐름까지, 플레이어가 체감하는 순간을 코드와 검증 과정으로 설명합니다.",
    heroMedia: "deck_image12.jpeg",
    order: ["projects", "infection", "flickdom", "network", "profile", "ownership", "ai", "contact"],
  },
  editorial: {
    number: "04",
    name: "CODE REVIEW",
    summary: "문제–판단–구현–결과를 읽기 좋은 기술 매거진형",
    heroLabel: "PORTFOLIO / PARK SHIN WOO",
    heroTitle: "코드보다 먼저\n판단 근거를 설명합니다",
    heroCopy: "기능 목록이 아니라 어떤 문제를 발견했고, 왜 그 구조를 선택했으며, 무엇으로 결과를 확인했는지 보여주는 케이스 스터디입니다.",
    heroMedia: "deck_image4.jpeg",
    order: ["profile", "infection", "network", "flickdom", "ownership", "projects", "ai", "contact"],
  },
  board: {
    number: "05",
    name: "FLICK BOARD",
    summary: "FlickDom의 색과 5×5 보드 규칙을 포트폴리오 언어로 확장한 개성형",
    heroLabel: "UNITY WEBGL / UE5 C++",
    heroTitle: "한 칸의 선택부터\n전체 게임 상태까지",
    heroCopy: "5×5 보드의 점령 규칙처럼, 작은 입력이 턴·점수·승패에 미치는 영향을 추적하며 구현합니다.",
    heroMedia: "flickdom_FlickDom.png",
    order: ["flickdom", "network", "ownership", "infection", "profile", "projects", "ai", "contact"],
  },
};

const fileForTheme = {
  signal: "candidate-01.html",
  blueprint: "candidate-02.html",
  cinematic: "candidate-03.html",
  editorial: "candidate-04.html",
  board: "candidate-05.html",
};

function boardCells() {
  return Array.from({ length: 25 }, (_, index) => {
    const owner = [2, 7, 18].includes(index) ? "blue" : [6, 13, 22].includes(index) ? "red" : "";
    return `<span class="board-cell ${owner}" aria-hidden="true"></span>`;
  }).join("");
}

function hero(config) {
  return `
    <section class="hero" id="top">
      <div class="hero-copy">
        <p class="kicker">${config.heroLabel}</p>
        <h1>${config.heroTitle.replace("\n", "<br>")}</h1>
        <p class="hero-lead">${config.heroCopy}</p>
        <div class="hero-links">
          <a href="mailto:tlsdn0403@gmail.com">tlsdn0403@gmail.com</a>
          <a href="https://github.com/tlsdn0403" target="_blank" rel="noreferrer">github.com/tlsdn0403 ↗</a>
        </div>
      </div>
      <figure class="hero-visual">
        <img src="${MEDIA + config.heroMedia}" alt="대표 프로젝트 플레이 화면">
        <figcaption><span>${config.number}</span>${config.name}</figcaption>
        <div class="mini-board" aria-label="FlickDom 5 곱하기 5 보드 모티프">${boardCells()}</div>
      </figure>
      <div class="hero-foot">
        <span>PARK SHIN WOO</span><span>CLIENT PROGRAMMER</span><span>2026 PORTFOLIO</span>
      </div>
    </section>`;
}

const sections = {
  profile: () => `
    <section class="section profile" id="profile">
      <header class="section-head">
        <p class="section-no">01 / PROFILE</p>
        <h2>구현 범위를 넓히되,<br>핵심은 상태와 상호작용입니다.</h2>
      </header>
      <div class="profile-layout">
        <p class="intro-copy">Unreal Engine 5에서는 C++ 기반 전투·피격·Vehicle Interaction을, Unity에서는 C# 기반 Physics·UI·WebGL 멀티플레이를 구현했습니다. 기능을 만든 뒤에는 실행 흐름, 로그, 코드 캡처로 동작을 다시 확인합니다.</p>
        <dl class="skill-list">
          <div><dt>C++</dt><dd>객체지향 · STL · UE5 Gameplay</dd></div>
          <div><dt>C#</dt><dd>Unity Physics · UI · Network State</dd></div>
          <div><dt>Engine</dt><dd>Unreal Engine 5 · Unity 6</dd></div>
          <div><dt>Workflow</dt><dd>GitHub · Visual Studio · Codex · Unity MCP</dd></div>
        </dl>
      </div>
      <div class="proof-strip" aria-label="핵심 역량">
        <span>Turn FSM</span><span>Host Authority</span><span>Snapshot</span><span>Collision / Trace</span><span>WebGL Release</span>
      </div>
    </section>`,

  projects: () => `
    <section class="section projects" id="projects">
      <header class="section-head compact">
        <p class="section-no">02 / SELECTED WORK</p>
        <h2>플레이 경험을 완성한 두 프로젝트</h2>
      </header>
      <div class="project-ledger">
        <article class="project-row featured">
          <span class="project-index">01</span>
          <img src="${MEDIA}deck_image1.png" alt="감염: 죽음의 도시 로고">
          <div><p class="meta">UE5 · C++ · 4인 팀</p><h3>감염: 죽음의 도시</h3><p>좀비 신체 분리와 기어가기 전환, 트럭 상호작용을 담당한 협동 TPS.</p></div>
          <a href="https://github.com/tlsdn0403/SYJ" target="_blank" rel="noreferrer">CODE ↗</a>
        </article>
        <article class="project-row featured">
          <span class="project-index">02</span>
          <img src="${MEDIA}flickdom_FlickDom.png" alt="FlickDom 메인 화면">
          <div><p class="meta">UNITY · C# · WEBGL · 팀 프로젝트</p><h3>FlickDom</h3><p>5×5 보드 점령과 카드 패턴을 겨루는 1대1 물리 보드게임.</p></div>
          <a href="https://fantastic-pothos-5ab193.netlify.app/" target="_blank" rel="noreferrer">PLAY ↗</a>
        </article>
        <article class="project-row minor">
          <span class="project-index">03</span>
          <div><p class="meta">FOUNDATION</p><h3>2D FSM · TCP/IP</h3><p>Pico2D 상태 머신·충돌과 OpenGL 클라이언트/서버 패킷 처리.</p></div>
        </article>
      </div>
    </section>`,

  infection: () => `
    <section class="section infection" id="infection">
      <header class="section-head">
        <p class="section-no">CASE 01 / INFECTION</p>
        <h2>피격 지점을 ‘부위 상태’로 연결했습니다.</h2>
        <p class="section-summary">2025.12.20 — 2026.07.08 · UE5 / C++ · 4인 팀 / Client Programmer</p>
      </header>
      <div class="case-layout">
        <div class="case-story">
          <div class="story-step"><span>PROBLEM</span><h3>같은 공격도 맞은 부위에 따라 다른 반응이 필요했습니다.</h3><p>단순 체력 감소만으로는 팔다리 파괴와 이동 상태 변화를 자연스럽게 연결하기 어려웠습니다.</p></div>
          <div class="story-step"><span>DECISION</span><h3>HitResult의 BoneName을 상태 키로 사용했습니다.</h3><p>부위별 누적 피해를 관리하고 임계값에 도달하면 DismemberLimb을 호출했습니다. 양쪽 다리가 파괴되면 StartCrawling으로 전환해 애니메이션과 이동 상태를 함께 바꿨습니다.</p></div>
          <div class="story-step"><span>RESULT</span><h3>전투 피드백과 AI 상태 전이가 하나의 흐름으로 이어졌습니다.</h3><p>피격 → 부위 피해 누적 → 신체 분리 → 기어가기 전환을 플레이 화면에서 검증했습니다.</p></div>
        </div>
        <div class="case-media">
          <figure><img src="${MEDIA}deck_image2.jpeg" alt="좀비 신체 분리 상태 전환 설계"><figcaption>STATE FLOW / StartCrawling</figcaption></figure>
          <figure><img src="${MEDIA}deck_image4.jpeg" alt="좀비 신체 분리 결과 화면"><figcaption>PLAY RESULT / Dismemberment</figcaption></figure>
        </div>
      </div>
      <div class="truck-block">
        <div class="truck-copy">
          <p class="section-no">CASE 01-B / TRUCK INTERACTION</p>
          <h3>탑승 후 캐릭터가 차량과 함께 움직이지 않던 문제</h3>
          <p>충돌을 끄는 것만으로는 이동 기준이 바뀌지 않았습니다. 탑승 시 캐릭터의 이동 기준을 트럭에 연결하고, 하차 시 원래 기준으로 복원하는 흐름으로 정리했습니다.</p>
          <ul><li>아이템 적재</li><li>기관총 상호작용</li><li>트럭 운전</li></ul>
        </div>
        <figure class="video-slot">
          <img src="${MEDIA}deck_image11.jpeg" alt="트럭 상호작용 영상용 포스터 이미지">
          <figcaption><span>VIDEO SLOT</span><strong>Truck Interaction</strong><small>assets/media/truck-interaction.mp4 추가 예정</small></figcaption>
        </figure>
      </div>
    </section>`,

  flickdom: () => `
    <section class="section flickdom" id="flickdom">
      <header class="section-head">
        <p class="section-no">CASE 02 / FLICKDOM</p>
        <h2>규칙은 가볍게,<br>상태 소유권은 명확하게.</h2>
        <p class="section-summary">2026.07 — 2026.08 · Unity 6 / C# / WebGL · 1 vs 1</p>
      </header>
      <div class="flick-intro">
        <figure class="main-shot"><img src="${MEDIA}flickdom_intro_2-1.png" alt="FlickDom 카드 패턴과 보드 화면"><figcaption>3 STAGES · 9 CARDS · 5×5 BOARD</figcaption></figure>
        <div class="game-rules">
          <article><span>01</span><h3>FLICK</h3><p>디스크를 선택하고 방향과 힘을 정해 발사합니다.</p></article>
          <article><span>02</span><h3>CLAIM</h3><p>착지한 셀의 점령 가능 여부를 Host가 판정합니다.</p></article>
          <article><span>03</span><h3>MATCH</h3><p>보드 점령 상태와 카드 패턴이 일치하면 점수를 얻습니다.</p></article>
        </div>
      </div>
      <div class="role-focus">
        <p class="kicker">MY SCOPE</p>
        <h3>박신우 · Client / Server / Build</h3>
        <div class="scope-columns">
          <p><strong>Client</strong>5×5 보드 점령, Cell 선택·배치 후보, Card Pattern Matching, Stage 진행, Monkey·Camera, Main Menu</p>
          <p><strong>Server</strong>초기 동기화 기반 위에서 FSM 턴 흐름, 멀티플레이 상태 전환, Network 구조 수정</p>
          <p><strong>Build</strong>WebGL 빌드·배포 환경 구성, 브라우저 실행 검증, 최종 Release</p>
        </div>
      </div>
    </section>`,

  network: () => `
    <section class="section network" id="network">
      <header class="section-head">
        <p class="section-no">TECHNICAL CASE / NETWORK</p>
        <h2>Client는 요청하고,<br>Host가 결과를 확정합니다.</h2>
      </header>
      <div class="network-layout">
        <div class="network-copy">
          <p class="lead">P2 입력의 즉시성과 물리 결과의 일관성을 함께 지키기 위해, 입력 요청과 최종 상태 Snapshot의 역할을 분리했습니다.</p>
          <ol class="network-flow">
            <li><span>CLIENT INPUT</span><p>방향·힘 계산 후 로컬 예측 시작</p></li>
            <li><span>FLICK REQUEST</span><p>owner · pieceId · impulse · shotId 전송</p></li>
            <li><span>HOST VALIDATE</span><p>턴 · 소유자 · 말 ID · 힘 범위 검증</p></li>
            <li><span>RECONCILE</span><p>Transform / PhysicsSettled Snapshot 적용</p></li>
          </ol>
        </div>
        <div class="state-map" role="img" aria-label="Client 요청에서 Host 검증과 최종 Snapshot으로 이어지는 흐름">
          <div class="state-node client"><small>P2 CLIENT</small><strong>Predict</strong><span>Input feels immediate</span></div>
          <span class="state-arrow">REQUEST →</span>
          <div class="state-node host"><small>HOST</small><strong>Validate + Simulate</strong><span>Single source of truth</span></div>
          <span class="state-arrow">SNAPSHOT →</span>
          <div class="state-node client"><small>P2 CLIENT</small><strong>Reconcile</strong><span>PhysicsSettled</span></div>
        </div>
      </div>
      <div class="state-split">
        <article><span>BoardState</span><p>5×5 owner grid를 반영</p></article>
        <article><span>ScoreState</span><p>점수와 승리자를 Host가 확정</p></article>
        <article><span>CardState</span><p>Stage · seed · claimedCards 비교</p></article>
        <article><span>Stale Guard</span><p>늦게 도착한 이전 상태를 거부</p></article>
      </div>
    </section>`,

  ownership: () => `
    <section class="section ownership" id="ownership">
      <header class="section-head compact">
        <p class="section-no">TEAM OWNERSHIP</p>
        <h2>함께 만든 결과에서 ‘내가 한 일’을 분리했습니다.</h2>
      </header>
      <div class="ownership-table">
        <article><p class="person">임찬진</p><h3>기획 · 입력 · 초기 동기화 기반</h3><p>게임 규칙, Drag/Flick, Trajectory, 사운드, 초기 Host/Client 기반과 턴·점수 상태 관리.</p></article>
        <article class="mine"><p class="person">박신우 / MY SCOPE</p><h3>보드 · 패턴 · 턴 FSM · Network 수정 · WebGL</h3><p>점령·배치, 카드 패턴과 Stage, 멀티 상태 전환, 네트워크 구조 개선, 빌드·배포·브라우저 검증.</p></article>
        <article><p class="person">황인성</p><h3>Material · Shader · 3D/2D Art</h3><p>Board와 Disk 리소스, Scene Prefab, HUD, Rule Screen, Victory UI와 표면 표현.</p></article>
      </div>
      <p class="ownership-note">포트폴리오의 Network 사례는 팀의 초기 기반 전체를 내 작업으로 표현하지 않고, 그 위에서 직접 수정한 FSM·상태 전환·Snapshot 적용 경계를 설명합니다.</p>
    </section>`,

  ai: () => `
    <section class="section ai" id="ai">
      <header class="section-head">
        <p class="section-no">AI WORKFLOW</p>
        <h2>AI 제안은 빠르게,<br>최종 판단은 실행 결과로.</h2>
      </header>
      <div class="ai-layout">
        <div class="ai-copy">
          <article><span>CONTEXT</span><h3>MD 기반 작업 맥락</h3><p>Architecture, Gameplay Rules, Server Plan, WebGL Build 문서로 요구사항과 변경 경계를 정리했습니다.</p></article>
          <article><span>ASSIST</span><h3>Codex · Unity MCP</h3><p>문서 비교, 구현 누락 점검, Editor 오브젝트·컴포넌트 확인에 활용했습니다.</p></article>
          <article><span>VERIFY</span><h3>코드 · 로그 · 실행 화면</h3><p>네트워크 판정과 빌드 결과는 실제 실행 흐름으로 다시 검증했습니다.</p></article>
          <p class="team-tool-note">팀 제작 흐름에서는 Blender/Substance MCP와 VARCO AI Sound도 리소스·사운드 제작에 활용했습니다.</p>
        </div>
        <div class="ai-media">
          <figure><img src="${MEDIA}flickdom_Project_MD.png" alt="FlickDom MD 기반 문서 구조"><figcaption>PROJECT CONTEXT</figcaption></figure>
          <figure><img src="${MEDIA}flickdom_Unity_MCP.png" alt="Unity MCP 작업 화면"><figcaption>EDITOR ASSIST</figcaption></figure>
          <figure><img src="${MEDIA}flickdom_Varco_EffectSound.png" alt="VARCO 효과음 제작 화면"><figcaption>TEAM AI SOUND</figcaption></figure>
        </div>
      </div>
    </section>`,

  contact: () => `
    <section class="section contact" id="contact">
      <p class="section-no">END / CONTACT</p>
      <h2>플레이어가 느끼는 차이를<br>구현으로 증명하겠습니다.</h2>
      <p>박신우 · Game Client Programmer</p>
      <div class="contact-links">
        <a href="mailto:tlsdn0403@gmail.com">EMAIL ↗</a>
        <a href="https://github.com/tlsdn0403" target="_blank" rel="noreferrer">GITHUB ↗</a>
        <a href="https://github.com/AACHANJINAA/FlickDom" target="_blank" rel="noreferrer">FLICKDOM CODE ↗</a>
        <a href="https://fantastic-pothos-5ab193.netlify.app/" target="_blank" rel="noreferrer">PLAY WEBGL ↗</a>
        <a href="https://www.youtube.com/watch?v=IR4KDTCyNKU" target="_blank" rel="noreferrer">DEMO VIDEO ↗</a>
      </div>
    </section>`,
};

function topbar(theme, config) {
  const links = Object.entries(variants).map(([key, value]) =>
    `<a href="${fileForTheme[key]}" ${key === theme ? 'aria-current="page"' : ""} title="${value.name}">${value.number}</a>`
  ).join("");

  return `
    <header class="topbar">
      <a class="back-link" href="index.html">← 5안 비교</a>
      <p><strong>${config.number}</strong> ${config.name}<span>${config.summary}</span></p>
      <nav aria-label="디자인 후보 전환">${links}</nav>
      <button type="button" class="print-button">PDF 저장</button>
    </header>`;
}

const theme = document.body.dataset.theme || "signal";
const config = variants[theme] || variants.signal;
document.title = `박신우 포트폴리오 · ${config.name}`;
document.querySelector("#app").innerHTML = topbar(theme, config) + `<main>${hero(config)}${config.order.map((key) => sections[key]()).join("")}</main>`;
document.querySelector(".print-button").addEventListener("click", () => window.print());

