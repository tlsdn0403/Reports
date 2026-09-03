---
document_type: portfolio_content_source
owner: 박신우
target_role: 게임 클라이언트 프로그래머
language: ko-KR
canva_design_id: DAHTqqFCz6Q
canva_edit_url: https://www.canva.com/design/DAHTqqFCz6Q/EueCEQ9F2-FIE1tnkIRYZw/edit
canva_title: 박신우_넥토리얼_클라이언트_포트폴리오
canva_pages_checked: 8
last_compiled: 2026-08-31
status: draft-needs-fact-check
---

# 박신우 게임 클라이언트 포트폴리오 콘텐츠 원본

## 이 문서의 용도

이 문서는 Canva 포트폴리오와 로컬 작업 폴더에 있는 기존 HTML, 발표 자료, 보고서, 자기소개서, 이미지 자료를 하나로 정리한 콘텐츠 원본이다.

- 이 문서에 있는 경력과 프로젝트 설명은 포트폴리오에 사용할 콘텐츠다.
- `확인 필요`, `추가 측정 필요`, `코드 캡처 필요`, `영상 필요` 표시는 삭제하거나 임의의 내용으로 채우지 않는다.
- 수치, 팀 규모, 개발 기간, 성과를 임의로 만들어내지 않는다.
- Canva 디자인은 시각적 기준으로 사용하고, 이 문서는 문구와 정보 구조의 기준으로 사용한다.
- 프로젝트 설명은 기능 나열보다 `문제 → 원인 분석 → 해결 → 검증 → 배운 점` 순서로 표현한다.

## 자료 우선순위

내용이 서로 다를 경우 다음 순서로 판단한다.

1. 현재 Canva 디자인에 직접 입력된 최신 정보
2. `new_portfolio/박신우_게임클라이언트_포트폴리오.html`
3. `canva_reference_portfolio_compact/index.html`
4. `extracted_text_v2/`에 있는 발표 자료와 보고서 추출문
5. 자기소개서 초안 및 과거 포트폴리오

---

# 1. 기본 정보

## 이름 및 지원 분야

- 이름: 박신우
- 영문명: Park Shin Woo
- 포지션: Game Client Programmer
- 지원 분야: 신입/주니어 게임 클라이언트 프로그래머
- 이메일: `tlsdn0403@gmail.com`
- 전화번호: `010-7390-1751`
- GitHub: <https://github.com/tlsdn0403>
- 학력: 한국공학대학교 게임공학과
- 졸업 예정: 2027년 3월 `확인 필요`

> 공개용 웹 포트폴리오에서는 전화번호 노출 여부를 최종 확인한다.

## 대표 소개 문구

### 짧은 문구

문제를 끝까지 따라가 플레이 경험으로 바꾸는 게임 클라이언트 개발자.

### 표지용 문구

UE5 C++와 Unity C#을 기반으로 플레이 중 발생하는 문제를 추적하고, 구조적인 수정으로 게임 경험까지 연결하는 개발자를 지향합니다.

### 소개 페이지용 문구

기능을 완성했다고 끝내지 않고, 실제 플레이에서 드러나는 충돌, 상태 전환, 물리, 네트워크 동기화 문제를 근거로 추적합니다. 입력부터 화면에 나타나는 결과까지 자연스럽게 이어지는 구조를 고민하며, 코드와 실행 결과로 구현을 설명할 수 있는 개발자를 목표로 합니다.

## 개발자로서의 방향성

- 플레이어 입력과 게임 시스템을 안정적으로 연결한다.
- 화면에 나타난 증상만 고치지 않고 충돌, 이동 기준, 상태, 네트워크 구조까지 추적한다.
- 기능의 소유권과 코드 경계를 명확히 설명한다.
- AI 도구의 결과를 그대로 채택하지 않고 코드, 로그, 실행 화면으로 재검증한다.

---

# 2. 기술 스택

## C++ / Unreal Engine 5

- C++ 객체지향 문법과 STL을 활용한 게임 로직 구현
- Actor / Component 구조
- Collision Channel / Trace / `FHitResult`
- BoneName 기반 피격 판정
- Behavior Tree와 NavMesh 기반 AI 이동
- Level Streaming과 타일 재사용 구조
- Blueprint와 C++ 연동
- 움직이는 플랫폼의 이동 기준과 `SetBase` 처리

## C# / Unity

- Unity 기반 게임 시스템 구현
- UI/UX, Physics, WebGL 클라이언트 개발
- FSM 기반 턴 진행
- 5x5 보드 점령과 카드 패턴 판정
- Host Authority 기반 멀티플레이 상태 관리
- Client Prediction과 Snapshot 보정
- WebGL 빌드와 정적 배포 환경 검증
- Netcode for GameObjects / Relay 사용 경험 `표기 범위 확인 필요`

## Network

- Host / Client 구조
- 요청 검증과 서버 권위 상태 확정
- BoardState / ScoreState / CardState Snapshot
- TCP/IP Socket 기반 Client / Server 패킷 송수신
- C2S / S2C 캐릭터 상태 전달
- AABB Collision 결과 반영

## Python / Pico2D

- Game Loop 구성
- State Machine과 Behavior Tree
- 입력, Update, Collision, Draw 단계 구성
- 3개 스테이지 진행과 Clear / Fail / Retry 상태 관리

## 협업 및 도구

- Git / GitHub
- 브랜치 관리와 커밋 단위 정리
- Git Flow 기반 협업
- 누락 커밋의 해시 추적과 cherry-pick 복구 경험
- 주차별 보고서와 Markdown 기반 작업 기록
- Visual Studio

## AI 및 제작 보조 도구

- Codex: 문서 정리, 구현 누락 점검, 코드 검토 보조
- Unity MCP: Editor 오브젝트와 컴포넌트 확인 보조
- Blender MCP: 보드, 디스크, 소품 제작 과정 보조
- Substance MCP: UV 스케일과 재질 작업 보조
- VARCO AI: UI 효과음과 BGM 제작 보조

AI 도구는 구현의 최종 판단자로 사용하지 않았다. 결과는 코드 흐름, 엔진 실행 결과, 로그, 브라우저 빌드, 팀 테스트를 기준으로 다시 확인했다.

---

# 3. 프로젝트 목록

| 우선순위 | 프로젝트 | 핵심 기술 | 포트폴리오 역할 |
|---|---|---|---|
| 1 | 감염: 죽음의 도시 | UE5, C++, Collision, BoneName, AI, Level Streaming | 대표 게임플레이 및 디버깅 사례 |
| 2 | FlickDom | Unity, C#, WebGL, Host Authority, Snapshot | 대표 네트워크 및 턴 시스템 사례 |
| 3 | NGP Fall Guys Network | C++, OpenGL, TCP/IP, Packet, AABB | 네트워크 기초 구현 사례 |
| 4 | Hamtori Escape | Python, Pico2D, Game Loop, FSM, Collision | 게임 클라이언트 기본기 사례 |

---

# 4. Project 01 — 감염: 죽음의 도시

## 프로젝트 개요

- 영문명: Infection: City of Death
- 형태: 협동 TPS 졸업작품
- 장르: Co-op TPS / Zombie Survival
- 엔진 및 언어: Unreal Engine 5 / C++
- 팀 구성: 4인 팀 / Client Programmer `현재 Canva 기준, 확인 필요`
- 개발 기간: 2025.12.20 - 2026.07.08 `현재 Canva 기준, 확인 필요`
- GitHub: <https://github.com/tlsdn0403/SYJ>
- 핵심 역할: 전투 피격, 좀비 상태, 트럭 상호작용, 2스테이지 진행 구조

### 한 문장 설명

1스테이지에서 탈출에 필요한 아이템을 파밍하고, 2스테이지에서는 트럭으로 이동하며 함께 탈출하는 UE5/C++ 기반 협동 좀비 TPS입니다.

### 소개 문단

제한된 시간 안에서 실제 플레이 가능한 전투와 탈출 흐름을 만들기 위해 총기 피격, 좀비 신체 분리, 차량 상호작용, 좀비 AI, 2스테이지 맵 진행 구조를 연결했습니다. 구현 과정에서 나타난 충돌과 이동 기준 문제를 코드 한 부분이 아닌 물리, 애셋, 상태 전환, 네트워크 관점에서 추적했습니다.

## 담당 역할

### 전투 및 피격

- LineTrace 기반 총기 발사
- `FHitResult` 전달
- BoneName 기반 부위별 피격 판정
- 부위별 내구도 관리
- 신체 분리 및 기어가기 상태 전환

### 트럭 상호작용

- Driver / Cargo / Turret 접근 타입 분리
- 운전석 조작권 전환
- 아이템 적재
- 적재함 탑승
- 거치형 기관총 사용
- 움직이는 트럭 위 플레이어의 이동 기준 처리

### 좀비 AI 및 스테이지

- Behavior Tree 기반 추격 흐름
- NavMesh / NavLinkProxy / FallZone 기반 이동 보완
- 2스테이지 타일 진행 구조
- Level Streaming Dynamic 실험
- 미리 로드한 타일을 재배치하는 Pool 방식으로 변경

## Technical Case 01 — BoneName 기반 좀비 신체 분리

### 문제

총알이 좀비의 Skeletal Mesh보다 Capsule Collision에 먼저 맞으면서 `FHitResult.BoneName`이 `None`으로 전달되는 문제가 발생했습니다. 단순 HP 감소만으로는 머리, 팔, 다리 같은 부위 파괴와 하체 절단 후 상태 전환을 구현하기 어려웠습니다.

### 원인 분석

- 총알과 Capsule의 Collision Channel 관계
- Skeletal Mesh의 피격 판정 설정
- `FHitResult` 전달 경로
- BoneName과 부위 내구도 데이터 연결 상태

### 해결

1. 총알과 Capsule의 충돌 채널을 분리했습니다.
2. Skeletal Mesh에서 실제 피격 판정을 받도록 수정했습니다.
3. `ApplyPointDamage`에서 `FHitResult`를 전달했습니다.
4. `OnZombieDamaged`에서 BoneName으로 피격 부위를 식별했습니다.
5. `TMap<FName, float>`로 머리, 팔, 다리, 척추 부위의 내구도를 관리했습니다.
6. 내구도가 0 이하가 되면 `DismemberLimb`에서 Constraint 해제, Bone 숨김, 물리 및 Impulse를 적용했습니다.
7. 다리 계열 Bone이 분리되면 `StartCrawling`으로 전환해 Capsule 크기와 이동 속도를 변경했습니다.

### 결과

피격 위치에 따라 머리 분리, 팔 분리, 하체 절단, 사망, 기어가기 상태 전환이 화면에 반영되도록 구현했습니다.

### 결과 흐름

`ApplyPointDamage → OnZombieDamaged → 부위 내구도 감소 → DismemberLimb / StartCrawling`

### 배운 점

게임플레이 버그는 코드만 확인해서 해결되지 않을 수 있으며 Collision 설정, Asset 구조, Animation 상태까지 함께 추적해야 합니다.

### 사용할 이미지

- `new_portfolio/assets/deck_image4.jpeg` — 좀비 피격 및 신체 분리 화면
- `new_portfolio/assets/deck_image5.jpeg` — 캐릭터 피격 테스트
- `new_portfolio/assets/deck_image7.jpeg` — 피격 구조 자료
- `new_portfolio/assets/deck_image8.jpeg` — 피격 구조 자료

### 추가할 증거

- `ApplyPointDamage` 코드 10~20줄 `코드 캡처 필요`
- BoneName으로 내구도를 찾는 코드 `코드 캡처 필요`
- `DismemberLimb`와 `StartCrawling` 전환 코드 `코드 캡처 필요`
- 신체 분리 전후 영상 `영상 필요`

## Technical Case 02 — 트럭 상호작용 구조

### 문제

초기에는 트럭 주변의 상호작용이 하나의 입력 흐름에 섞여 있어 운전, 탑승, 적재, 기관총 사용이 서로 충돌했습니다.

### 해결

접근 위치별 Trigger에 Driver, Cargo, Turret 타입을 부여하고, 플레이어가 상호작용 키를 눌렀을 때 Trigger 타입에 따라 서로 다른 행동을 호출하도록 분리했습니다.

### 상호작용 흐름

`상호작용 입력 → 접근 Trigger 타입 판별 → Truck 상태 전환 → 운전 / 탑승 / 적재 / 무기 사용`

### 결과

- Driver Trigger: 운전석 조작권 전환
- Cargo Trigger: 아이템 적재와 적재함 탑승
- Turret Trigger: 트럭 기관총 사용
- 파밍 이후 이동과 전투 흐름을 하나의 차량 시스템으로 연결

### 사용할 이미지

- `new_portfolio/assets/deck_image9.jpeg` — 트럭 적재
- `new_portfolio/assets/deck_image10.jpeg` — 트럭 전면 또는 운전석
- `new_portfolio/assets/deck_image11.jpeg` — 적재함 탑승
- `new_portfolio/assets/deck_image12.jpeg` — 트럭 주행

## Technical Case 03 — 움직이는 트럭 위 이동 기준 디버깅

### 증상

트럭 적재함에 탑승한 플레이어가 트럭 이동 중 하늘로 튀거나 뒤로 밀리는 문제가 발생했습니다.

### 분석 과정

1. 트럭 Mesh와 플레이어 Mesh 간 물리 충돌을 의심했습니다.
2. 충돌을 분리하고 별도 플랫폼과 투명 벽을 구성해 튀는 현상을 줄였습니다.
3. 이후 플레이어가 월드 좌표를 유지해 트럭 뒤로 밀리는 현상을 확인했습니다.
4. 단순 위치 보정은 물리와 네트워크 보정이 다시 충돌할 가능성이 있다고 판단했습니다.

### 해결

- 트럭 위에 있을 때 `SetBase(NewBase)`로 트럭 바닥을 플레이어의 이동 기준으로 지정했습니다.
- 점프 또는 하차 시 `SetBase(nullptr)`를 호출했습니다.
- 탑승과 관련된 상태를 명시적으로 초기화했습니다.

### 결과

플레이어가 움직이는 트럭의 이동을 자연스럽게 따라가도록 개선하고, 점프와 하차 시 남아 있던 순간적인 위치 보정 문제를 줄였습니다.

### 추가할 증거

- `SetBase(NewBase)` / `SetBase(nullptr)` 코드 `코드 캡처 필요`
- 문제 발생 전후 비교 영상 `영상 필요`

## Technical Case 04 — 2스테이지 타일 진행 구조

### 초기 접근

TileMarker의 Entry, Trigger, Exit Point를 기준으로 트럭이 Next Tile Trigger에 도착하면 다음 타일을 `ULevelStreamingDynamic`으로 로드했습니다.

### 문제

플레이 도중 다음 타일을 동적으로 로드할 때 순간적인 멈춤이 발생했습니다.

### 구조 변경

1. 2스테이지 시작 시 사용할 타일을 미리 생성했습니다.
2. 생성한 타일을 Pool에 등록하고 플레이어 시야 밖에 배치했습니다.
3. 다음 타일이 필요하면 새로 로드하지 않고 Pool에서 꺼냈습니다.
4. Entry / Exit 기준으로 타일 위치를 재배치했습니다.
5. 오래된 타일은 삭제하지 않고 Pool로 돌려보냈습니다.

### AI 이동 보완

NavMesh, NavLinkProxy, FallZone을 이용해 건물 위 좀비가 트럭 진행에 맞춰 추격하고 낙하하도록 조정했습니다.

### 결과

Next Tile Trigger 시점의 동적 로드 부담을 줄이고, 무한 맵 연결 흐름을 안정화했습니다. 정량적인 프레임타임 개선 수치는 아직 문서에 없으므로 임의로 기재하지 않습니다.

### 사용할 이미지

- `new_portfolio/assets/deck_image13.jpeg` — 타일 설계 또는 트럭 장면
- `new_portfolio/assets/deck_image14.jpeg` — 스테이지 맵
- `new_portfolio/assets/deck_image15.jpeg` — 2스테이지 플레이
- `new_portfolio/assets/deck_image20.png` — 구조 설명 자료

## 감염 프로젝트 문제 해결 프레임

1. 증상 재현: 튕김, 미동작, 추격 실패를 반복 확인
2. 상태 추적: HitResult, Collision, BT Task, Vehicle 상태를 구간별 확인
3. 원인 분리: 코드, 물리, Asset, Navigation 중 문제가 발생한 층을 분리
4. 구조 변경: Collision Channel, Trigger 타입, Tile Pool 등 구조를 수정
5. 플레이 검증: 실행 화면과 반복 테스트로 수정 결과 확인

---

# 5. Project 02 — FlickDom

## 프로젝트 개요

- 형태: 팀 프로젝트 / NAN2026 NHN GAME × AI Hackathon
- 장르: 1대1 물리 기반 전략 플릭 보드게임
- 엔진 및 언어: Unity / C#
- 플랫폼: WebGL
- 개발 기간: 2026.07 `현재 Canva 기준`
- 팀 구성: 3인 팀 `팀 역할 문서 기준`
- 핵심 역할: Client / Server / Build
- GitHub: <https://github.com/AACHANJINAA/FlickDom>
- WebGL: <https://fantastic-pothos-5ab193.netlify.app/>
- Demo Video: <https://www.youtube.com/watch?v=IR4KDTCyNKU>

### 한 문장 설명

디스크를 튕겨 5x5 보드 칸을 점령하고, 카드 패턴과 보드 상태가 일치하면 점수를 얻는 Unity WebGL 1대1 보드게임입니다.

### 게임 규칙

- 디스크를 보드 위에 배치해 카드가 요구하는 패턴을 완성합니다.
- Easy 카드는 1점, Normal 카드는 2점, Hard 카드는 3점입니다.
- 매치는 3개 Stage로 진행됩니다.
- 9장의 카드를 시작 시 한 번 섞고 Stage마다 3장씩 사용합니다.
- 카드 패턴을 완성해 점수를 얻고 10점에 먼저 도달하면 승리합니다.

## 박신우 담당 범위

### Client

- 5x5 Board 점령 로직
- Cell 선택과 배치 후보 처리
- Card Pattern Matching
- Stage 진행
- Monkey 조작과 Camera 흐름
- Main Menu 제작
- Client Prediction 적용

### Server / Network

- FSM 기반 턴 흐름
- 멀티플레이 상태 전환
- Network 구조 수정
- FlickRequest / PlacementRequest 검증
- BoardState / ScoreState / CardState Snapshot
- Host 기준 최종 상태 확정

### Build

- WebGL Build 및 배포 환경 구성
- 브라우저 실행 검증
- 최종 Release

## Technical Case 01 — Host 권위 턴 구조

### 문제

Client가 턴, 점수, 보드 결과를 각자 확정하면 Host와 다른 결과가 발생할 수 있습니다. 네트워크 지연으로 이전 Stage의 Snapshot이 늦게 도착하면 카드와 점수가 과거 상태로 되돌아갈 수도 있습니다.

### 해결

- 턴 시작, Flick 요청, 물리 안정화, 점수 계산, 다음 턴 전환을 Host 기준으로 확정했습니다.
- Client는 입력 의도만 요청으로 전송합니다.
- Host가 현재 턴, 소유자, 말 ID, 입력 값, 배치 가능 여부를 검증합니다.
- 검증된 결과를 Snapshot으로 Client에 전달합니다.
- Client는 이전 Revision의 stale Snapshot을 거부하고 화면만 갱신합니다.

## Technical Case 02 — P2 Client Prediction과 Host 최종 판정

### 문제

P2가 디스크를 튕긴 직후 Client 화면에서는 즉시 움직임이 보여야 하지만 최종 결과는 Host 물리가 결정해야 했습니다. Host Transform만 기다리면 입력 반응이 늦고, Client 물리를 그대로 신뢰하면 Host와 결과가 달라집니다.

### 해결 흐름

1. Client가 입력 직후 로컬 예측을 시작합니다.
2. 방향과 힘을 정규화한 뒤 Host에 FlickRequest를 보냅니다.
3. Host가 현재 턴, 소유자, 말 ID, impulse 범위를 검증합니다.
4. 움직이는 동안 Transform Snapshot으로 상태를 전달합니다.
5. 정착 이후 PhysicsSettled Snapshot을 전달합니다.
6. Client는 Host의 최종 결과로 보정하고 예측 상태를 종료합니다.

### 결과

입력 직후의 반응성을 유지하면서도 최종 위치와 게임 판정은 Host 기준으로 맞추는 흐름을 구성했습니다.

### 추가할 증거

- Prediction 적용 전후 위치 오차 `추가 측정 필요`
- RTT 평균 `추가 측정 필요`
- Snapshot 처리 로그 `추가 측정 필요`
- P2 Flick 예측과 보정 전후 영상 `영상 필요`

## Technical Case 03 — Board / Score / Card Snapshot

### BoardState

5x5 보드의 칸 점령자를 관리하고, 디스크 충돌 이후 최종 칸 소유권을 계산했습니다.

### ScoreState

카드 패턴과 보드 상태가 일치하는지 Host에서 검사하고, 점수 반영 시점을 통제했습니다.

### CardState

초기 9장 카드 셔플과 Stage별 3장 배분 결과를 모든 Client에서 동일하게 유지했습니다.

### 요청 검증

- FlickRequest: 현재 턴, 소유자, 말 ID, 방향과 힘 범위 검증
- PlacementRequest: 배치 가능 Cell, 점령 가능 여부, 재배치 source 검증

### 설계 이유

Board, Score, Card 상태를 분리해 각 상태의 변경 주기와 책임을 명확히 하고, 문제가 발생했을 때 어느 Snapshot에서 값이 달라졌는지 추적할 수 있게 했습니다.

## FlickDom 결과

- Host / Client 기반 2인 멀티플레이
- Lobby와 방 코드 기반 연결
- 역할 배정과 턴 진행
- 보드, 카드, 점수 동기화
- 카드 획득 애니메이션과 카드 공개 연출
- 효과음과 BGM 적용
- WebGL 배포 및 브라우저 실행

## FlickDom에서 배운 점

- 네트워크 게임에서는 누가 결과를 확정하는지 명확해야 합니다.
- 입력 반응성과 상태 정합성을 동시에 고려해야 합니다.
- Snapshot의 책임과 Revision 기준이 분명해야 stale data를 다룰 수 있습니다.
- AI를 사용했다는 사실보다 결과를 어떻게 검증했는지가 중요합니다.

## 사용할 이미지

- `new_portfolio/assets/flickdom_FlickDom.png` — 메인 화면
- `new_portfolio/assets/flickdom_intro_2-1.png` — 카드 목표 화면
- `new_portfolio/assets/flickdom_intro_2-2.png` — 보드 화면
- `new_portfolio/assets/flickdom_intro_2-3.png` — 승리 화면
- `new_portfolio/assets/flickdom_intro_3-1.png` — 멀티플레이 로비
- `new_portfolio/assets/flickdom_intro_3-4.png` — 방 코드 화면
- `new_portfolio/assets/flickdom_intro_4-1.png` — 실행 화면
- `new_portfolio/assets/flickdom_Project_MD.png` — 문서 기반 개발 화면
- `new_portfolio/assets/flickdom_Unity_MCP.png` — Unity MCP 화면
- `new_portfolio/assets/flickdom_Blender_MCP.png` — Blender MCP 화면
- `new_portfolio/assets/flickdom_Substance_MCP.png` — Substance MCP 화면
- `new_portfolio/assets/flickdom_Varco_EffectSound.png` — 효과음 제작 화면
- `new_portfolio/assets/flickdom_Varco_BGM.png` — BGM 제작 화면

---

# 6. Project 03 — NGP Fall Guys Network

## 프로젝트 개요

- 형태: 네트워크 게임 프로그래밍 수업 프로젝트
- 장르: Fall Guys 스타일 장애물 경주 게임
- 언어 및 그래픽: C++ / OpenGL
- 네트워크: TCP/IP Socket
- 목표: 기존 로컬 플레이 구조를 3인 네트워크 플레이 구조로 전환
- GitHub: <https://github.com/tlsdn0403/NGP_Project>

### 한 문장 설명

C++ OpenGL 기반 장애물 게임을 TCP/IP Client / Server 구조로 전환하며 캐릭터 상태 전달과 충돌 처리의 기초를 구현한 프로젝트입니다.

## 구현 내용

- 접속 순서에 따라 캐릭터 번호 부여
- 로컬 플레이어 입력과 이동 상태 수집
- C2S_Character 패킷으로 서버에 상태 전송
- 서버 기준 상태 갱신
- S2C_Character 패킷으로 다른 Client에 상태 전달
- 캐릭터 위치와 이동 방향 반영
- 캐릭터-캐릭터 및 캐릭터-장애물 AABB Collision
- 장애물 상태 공유

## 상태 전달 흐름

`Input → C2S Packet → Server Update → S2C Packet → Client Render / Collision`

## 배운 점

엔진 없이 입력, 네트워크, 충돌, 렌더링 순서를 직접 다루며 Unity와 Unreal이 내부적으로 감싸는 하위 흐름을 이해했습니다. 패킷 구조와 상태 갱신 단계를 나누어야 값이 달라지는 지점을 추적하기 쉽다는 점을 배웠습니다.

## 사용할 이미지

- `new_portfolio/assets/deck_image21.png` — 네트워크 게임 화면
- `new_portfolio/assets/deck_image20.png` — 서버 / 클라이언트 흐름 자료

## 검증 메모

팀 진행 보고서와 기존 포트폴리오 사이에 개인 구현 범위 표현 차이가 있습니다. 최종본에서는 본인이 직접 구현한 Packet, Collision, Viewport 범위를 코드 또는 커밋으로 다시 확인합니다.

---

# 7. Project 04 — Hamtori Escape

## 프로젝트 개요

- 형태: 2D 게임 프로그래밍 수업 프로젝트
- 장르: 2D 탈출 게임
- 언어 및 라이브러리: Python / Pico2D
- GitHub: <https://github.com/tlsdn0403/2DGP-Project>
- 발표 영상: <https://www.youtube.com/watch?v=lTstJrENbkI> `영상 대상 확인 필요`

### 한 문장 설명

햄토리를 조작해 스테이지마다 다른 위험 요소를 피하고 출구까지 이동하는 2D 탈출 게임입니다.

## 스테이지 구성

- Stage 1: 구르는 돌을 피해 위쪽 탈출구로 이동
- Stage 2: NPC의 추격과 배회 패턴을 피해 출구까지 이동
- Stage 3: NPC를 돌에 유도해 제거한 뒤 돌과 NPC를 피해 탈출
- Ending: 최종 탈출 후 종료 화면

## 구현 내용

- Player 입력과 이동
- Game Loop
- Collision 판정
- NPC State Machine과 Behavior Tree
- 추격 / 배회 상태 전환
- Clear / Fail / Retry 흐름
- Stage 및 Ending 전환
- Camera와 화면 갱신

## 기본 흐름

`Input → Update → Collision → State Transition → Draw`

## 배운 점

작은 2D 프로젝트를 완성하면서 입력, 갱신, 충돌, 상태 전환, 렌더링을 단계별로 나누어 생각하는 습관을 만들었습니다. 이 경험은 이후 Unity와 Unreal 프로젝트에서 문제를 더 빠르게 분해하는 기반이 되었습니다.

## 사용할 이미지

- `new_portfolio/assets/deck_image16.png` — Stage 1
- `new_portfolio/assets/deck_image17.png` — Stage 2
- `new_portfolio/assets/deck_image18.png` — Stage 3
- `new_portfolio/assets/deck_image19.png` — Ending

---

# 8. 협업 경험

## 역할 경계 명확화

프로젝트별로 본인이 맡은 코드 경계를 정리하고, 팀 작업과 개인 작업을 구분해 설명할 수 있도록 문서화했습니다.

## Git 기반 협업

Git Flow를 사용하고, Merge 과정에서 사라진 커밋은 해시를 추적한 뒤 cherry-pick으로 복구했습니다. 커밋 단위와 작업 범위를 정리해 팀원이 변경 이유를 확인할 수 있도록 했습니다.

## 소통 문제 해결

선행 리팩터링 작업이 늦어지면서 다음 작업을 진행할 수 없고 팀원 간 소통이 끊긴 상황이 있었습니다. 한쪽의 잘못으로 판단하지 않고 완료된 작업, 남은 범위, 대기 중인 업무를 함께 정리하는 자리를 마련했습니다. 이후 일정 변경이나 어려움이 예상되면 완성 후가 아니라 중간 진행 상황부터 공유하기로 합의했고 프로젝트 진행을 정상화했습니다.

## 보고서 기반 회고

주차별 보고서를 일정 기록으로만 두지 않고 문제, 원인, 수정, 검증의 증거로 다시 정리했습니다.

---

# 9. AI 활용 경험

## 활용 원칙

AI는 핵심 구현의 소유권이나 최종 판단을 대신하지 않습니다. 가능한 원인을 나열하고, 문서를 정리하고, 누락 항목을 점검하는 보조 수단으로 사용합니다.

## 활용 사례

- 보고서, README, 포트폴리오 문구 재구성
- 프로젝트 구조와 Markdown 규칙 점검
- 충돌, 동기화, 상태 전환 문제의 원인 가설 정리
- Unity Editor 오브젝트와 컴포넌트 확인
- Blender와 Substance 작업 과정 보조
- UI 효과음과 BGM 제작 보조
- WebGL Release 조건 점검

## 검증 방식

- 코드 흐름 확인
- Unity / Unreal 실행 결과 확인
- 로그 비교
- WebGL 브라우저 실행
- 팀원 테스트
- 전후 영상과 Screenshot 비교

---

# 10. 링크 모음

| 구분 | 링크 | 상태 |
|---|---|---|
| 개인 GitHub | <https://github.com/tlsdn0403> | 사용 |
| 감염 GitHub | <https://github.com/tlsdn0403/SYJ> | 사용 |
| FlickDom GitHub | <https://github.com/AACHANJINAA/FlickDom> | 사용 |
| FlickDom WebGL | <https://fantastic-pothos-5ab193.netlify.app/> | 사용 |
| FlickDom Demo | <https://www.youtube.com/watch?v=IR4KDTCyNKU> | 사용 |
| Hamtori GitHub | <https://github.com/tlsdn0403/2DGP-Project> | 사용 |
| NGP GitHub | <https://github.com/tlsdn0403/NGP_Project> | 사용 |
| Reports | <https://github.com/tlsdn0403/Reports> | 사용 |
| YouTube 영상 | <https://www.youtube.com/watch?v=lTstJrENbkI> | 대상 프로젝트 확인 필요 |

---

# 11. Canva 현재 구성과 확장 방향

## 현재 Canva에서 확인된 8페이지

1. Cover — Park Shin Woo / Client Programmer / 이메일 / GitHub
2. Tech Stack — C++, Unreal Engine, Unity, GitHub, Visual Studio
3. Project Index
4. Project 01 감염: 죽음의 도시 Overview
5. 좀비 신체 분리
6. Truck Interaction
7. Project 02 FlickDom Overview
8. Thank You

## 권장 최종 페이지 구성

### Page 01 — Cover

- 제목: `GAME CLIENT PORTFOLIO`
- 이름: `Park Shin Woo`
- 직무: `Client Programmer`
- 이메일과 GitHub
- 대표 이미지: `new_portfolio/assets/deck_image1.png`

### Page 02 — Profile & Direction

- 제목: `문제를 끝까지 따라가 플레이 경험으로 바꾸는 개발자`
- 짧은 소개 문구
- 지원 분야와 학력
- 문제 해결 방향성 3개

### Page 03 — Tech Stack

- C++ / Unreal Engine 5
- C# / Unity
- Network
- Python / Pico2D
- Git / Visual Studio
- AI Tool은 별도 보조 도구로 짧게 표현

### Page 04 — Project Index

- 감염: 죽음의 도시
- FlickDom
- NGP Fall Guys Network
- Hamtori Escape

### Page 05 — 감염 Overview

- 장르, 기간, 구성, 엔진, 역할
- 한 문장 설명
- 대표 이미지

### Page 06 — 감염 Role

- 전투 피격
- 좀비 상태
- 트럭 상호작용
- 2스테이지

### Page 07 — 감염 BoneName Case

- 문제
- 원인
- 해결 흐름
- 결과 이미지

### Page 08 — 감염 Truck Case

- Trigger 타입 분리
- Driver / Cargo / Turret
- 상호작용 흐름

### Page 09 — 감염 Moving Base Debugging

- 플레이어가 튀거나 뒤로 밀리는 증상
- Collision 분리
- `SetBase(NewBase)`와 `SetBase(nullptr)`
- 전후 영상 또는 코드 증거

### Page 10 — 감염 Stage 2

- 동적 로드 문제
- Tile Pool 전환
- NavMesh / NavLink / FallZone
- 결과와 남은 측정 항목

### Page 11 — FlickDom Overview

- 게임 규칙
- Unity / C# / WebGL
- 역할: Network / Turn / Board / Build
- 대표 이미지

### Page 12 — FlickDom Ownership

- 본인 담당 코드 경계
- Board 점령
- Card Pattern Matching
- FSM Turn
- WebGL Release

### Page 13 — FlickDom Prediction

- Client Prediction 문제
- FlickRequest 검증
- Transform Snapshot
- PhysicsSettled 최종 보정

### Page 14 — FlickDom Board / Card Sync

- BoardState
- ScoreState
- CardState
- stale Snapshot 거부

### Page 15 — Other Projects

- NGP Fall Guys Network
- Hamtori Escape
- 프로젝트당 핵심 이미지 1개와 구현 증거 3개만 사용

### Page 16 — Collaboration & AI Tools

- Git 기반 협업
- 보고서 기반 회고
- AI 활용과 검증 방식

### Page 17 — Links & Evidence

- GitHub
- FlickDom WebGL
- Demo Video
- 코드 캡처와 보고서

### Page 18 — Closing

- `읽어주셔서 감사합니다.`
- `박신우 · 게임 클라이언트 프로그래머`
- 이메일과 GitHub

---

# 12. 최종 확인이 필요한 항목

- [ ] 감염 개발 기간: Canva의 `2025.12.20 - 2026.07.08`이 최종값인지 확인
- [ ] 감염 팀 구성: Canva의 `4인 팀`이 최종값인지 확인
- [ ] 학력의 `2027년 3월 졸업 예정` 표기 확인
- [ ] FlickDom 개발 기간을 월 단위가 아닌 정확한 날짜로 표기할지 확인
- [ ] FlickDom에서 NGO / Relay를 기술 스택에 직접 표기할지 확인
- [ ] `lTstJrENbkI` 영상이 감염 발표인지 Hamtori 발표인지 확인
- [ ] NGP 프로젝트의 개인 구현 범위를 커밋 또는 코드로 확인
- [ ] 공개 HTML에 전화번호를 노출할지 확인
- [ ] 감염 C++ 코드 캡처 추가
- [ ] FlickDom Prediction 전후 수치 또는 로그 추가
- [ ] 트럭 탑승 문제 전후 영상 추가

## 자료에 존재한 충돌 기록

### 감염 개발 기간

- 현재 Canva: `2025.12.20 - 2026.07.08`
- 자기소개서 포트폴리오: `2026.01.02 - 2026.07.06`
- 과거 HTML: `2025.12 - 2026.05`

현재 문서에서는 Canva 값을 우선 사용했지만 최종 제출 전 확인이 필요하다.

### 감염 팀 구성

- 현재 Canva: `4인 팀`
- 과거 중간 발표 자료: 박신우, 배주환, 안윤진 3인 표기

팀 구성 변경 가능성이 있으므로 최종 표기를 확인한다.

---

# 13. HTML 생성 시 콘텐츠 규칙

- 이 Markdown의 문구를 그대로 복사하기보다 페이지 크기에 맞게 압축하되 의미를 바꾸지 않는다.
- 한 페이지에는 핵심 주장 하나만 배치한다.
- 각 기술 사례는 문제, 해결, 결과가 모두 보여야 한다.
- 정량 수치가 없는 항목에는 임의의 개선율을 작성하지 않는다.
- 코드 캡처와 영상이 없는 항목은 Placeholder로 명확하게 남긴다.
- 팀 프로젝트에서는 반드시 박신우의 담당 범위를 별도로 표시한다.
- AI 활용 페이지는 프로젝트 구현 페이지보다 낮은 우선순위로 둔다.
- 대표 프로젝트 지면은 `감염: 죽음의 도시`와 `FlickDom`에 집중한다.
