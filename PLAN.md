# Mission 2 수행 계획 — 파이썬 퀴즈 게임

> `mission_2.md` 요구사항을 기준으로 작성한 단계별 실행 계획.
> 각 단계는 "구현 → 검증 → 커밋" 순서로 진행하며, 커밋 메시지 예시를 함께 명시한다.

---

## 1. 프로젝트 개요

- **목표**: 터미널에서 동작하는 퀴즈 게임을 Python으로 처음부터 끝까지 구현하고, Git/GitHub 워크플로우(커밋 10개 이상, 브랜치 병합, clone/pull)를 실습한다.
- **퀴즈 주제(제안)**: 영화 (예시 화면과 자연스럽게 어울리고 문제 만들기 쉬움 — 원하는 주제로 교체 가능)
- **개발 환경**: Python 3.10+, 외부 라이브러리 없이 표준 라이브러리만 사용

## 2. 최종 파일 구조

```
mission-2/
├── main.py          # 진입점: QuizGame 생성 후 run() 호출
├── quiz.py          # Quiz 클래스 (문제/선택지/정답 + 출력/정답확인 메서드)
├── quiz_game.py     # QuizGame 클래스 (메뉴, 각 기능, 저장/불러오기)
├── state.json       # 데이터 파일 (퀴즈 목록 + 최고 점수, UTF-8)
├── README.md        # 프로젝트 문서
├── .gitignore       # __pycache__, .venv 등
├── PLAN.md          # 이 문서
└── docs/screenshots/  # 제출용 스크린샷
```

파일을 3개로 분리하는 이유: "역할별 구조화" 요구사항을 파일 수준에서도 보여주고, 기능 단위 커밋을 만들기 쉽다. (단일 `main.py`로 합쳐도 요구사항 위반은 아님)

## 3. 클래스 설계

### `Quiz` (quiz.py) — 퀴즈 1개를 표현
| 구분 | 이름 | 설명 |
|---|---|---|
| 속성 | `question: str` | 문제 |
| 속성 | `choices: list[str]` | 선택지 4개 |
| 속성 | `answer: int` | 정답 번호 (1~4) |
| 메서드 | `display(number)` | 문제와 선택지 출력 |
| 메서드 | `check(user_answer) -> bool` | 정답 여부 판정 |
| 메서드 | `to_dict()` / `from_dict()` | JSON 저장/복원용 변환 |

### `QuizGame` (quiz_game.py) — 게임 전체 관리
| 구분 | 이름 | 설명 |
|---|---|---|
| 속성 | `quizzes: list[Quiz]` | 퀴즈 목록 |
| 속성 | `best_score: int \| None` | 최고 점수 (None = 아직 안 풂) |
| 메서드 | `run()` | 메인 루프: 메뉴 출력 → 선택 → 기능 실행 |
| 메서드 | `show_menu()` | 메뉴 화면 출력 |
| 메서드 | `play_quiz()` | 퀴즈 풀기 (출제, 채점, 결과, 최고점수 갱신) |
| 메서드 | `add_quiz()` | 퀴즈 추가 (입력 검증 포함) |
| 메서드 | `list_quizzes()` | 퀴즈 목록 출력 |
| 메서드 | `show_score()` | 최고 점수 확인 |
| 메서드 | `load_state()` / `save_state()` | state.json 읽기/쓰기 (try/except) |
| 메서드 | `read_int(prompt, min, max) -> int` | 공통 숫자 입력 헬퍼 (핵심!) |

### 공통 입력 처리 설계 (`read_int`)
숫자 입력이 필요한 모든 곳(메뉴 선택, 정답 입력, 정답 번호 입력)에서 하나의 헬퍼를 재사용:
1. `input().strip()` — 앞뒤 공백 제거
2. 빈 입력 → 안내 후 재입력
3. `int()` 변환 실패(`abc`) → 안내 후 재입력
4. 범위 밖(메뉴 9, 정답 0) → 안내 후 재입력

`KeyboardInterrupt`/`EOFError`는 `main.py`(또는 `run()`)에서 잡아서 → 안내 메시지 출력 → `save_state()` → 정상 종료.

### state.json 스키마
```json
{
  "quizzes": [
    {"question": "...", "choices": ["a", "b", "c", "d"], "answer": 2}
  ],
  "best_score": 80
}
```
- 파일 없음 → 기본 퀴즈 5개로 시작
- JSON 손상(`json.JSONDecodeError`) → 안내 메시지 + 기본 데이터로 복구
- 항상 `encoding="utf-8"`, `ensure_ascii=False` 사용

## 4. 단계별 실행 계획 (커밋 계획 포함)

총 12개 이상의 커밋이 나오도록 기능 단위로 쪼갠다.

### 0단계. 저장소 초기 설정
- [ ] GitHub에 새 저장소 생성 (예: `python-quiz-game`)
- [ ] 로컬 `git init` → 원격 연결 (`git remote add origin ...`)
- [ ] `.gitignore` 작성 (`__pycache__/`, `*.pyc`, `.venv/`, `.vscode/` — `state.json`은 제출물이므로 **포함**)
- [ ] `README.md` 뼈대 작성 (제목 + 개요 한 줄)
- 커밋 ①: `Init: 프로젝트 초기 설정 (.gitignore, README 뼈대)` → **push**

### 1단계. 메뉴 골격 (main 브랜치)
- [ ] `main.py` + `QuizGame` 최소 버전: 메뉴 출력, 번호 선택, 종료(5번), 잘못된 입력 처리
- [ ] `read_int` 헬퍼를 이 단계에서 먼저 구현 (이후 모든 입력에 재사용)
- 커밋 ②: `Feat: 메뉴 출력 및 선택/종료 기능 구현`
- 커밋 ③: `Feat: 공통 숫자 입력 검증 헬퍼 추가 (공백/빈입력/범위 처리)`

### 2단계. Quiz 클래스
- [ ] `quiz.py`에 `Quiz` 클래스 작성 (속성 3개 + display/check/to_dict/from_dict)
- 커밋 ④: `Feat: Quiz 클래스 정의 (문제/선택지/정답, 출력/채점 메서드)`

### 3단계. 기본 퀴즈 데이터
- [ ] 영화 주제 퀴즈 5개를 `Quiz` 인스턴스로 작성 (기본 데이터 함수 `default_quizzes()`)
- 커밋 ⑤: `Feat: 영화 주제 기본 퀴즈 5개 작성`

### 4단계. 퀴즈 풀기 — **브랜치 실습 구간**
- [ ] `git checkout -b feature/play-quiz` 로 브랜치 생성
- [ ] `play_quiz()` 구현: 순서대로 출제 → 정답 입력 → 즉시 정답/오답 표시 → 전체 결과(점수) 표시 → 퀴즈 0개인 경우 처리
- 커밋 ⑥ (브랜치에서): `Feat: 퀴즈 풀기 기능 구현 (출제/채점/결과 표시)`
- [ ] `git checkout main` → `git merge feature/play-quiz` → push
  (병합 커밋을 남기려면 `--no-ff` 사용 권장 → 그래프 스크린샷이 예쁘게 나옴)

### 5단계. 퀴즈 추가
- [ ] `add_quiz()`: 문제/선택지 4개/정답 번호(1~4) 입력 → `Quiz` 생성 → 목록에 추가 → **즉시 `save_state()`**
- [ ] 빈 문제/빈 선택지 입력 거부 처리
- 커밋 ⑦: `Feat: 퀴즈 추가 기능 구현 (입력 검증 + 저장)`

### 6단계. 퀴즈 목록
- [ ] `list_quizzes()`: 번호와 문제 출력, 0개인 경우 안내
- 커밋 ⑧: `Feat: 퀴즈 목록 조회 기능 구현`

### 7단계. 점수 확인
- [ ] `play_quiz()` 끝에 최고 점수 비교/갱신 + `save_state()` 연결
- [ ] `show_score()`: 최고 점수 출력, 아직 안 푼 경우(`best_score is None`) 안내
- 커밋 ⑨: `Feat: 최고 점수 기록/확인 기능 구현`

### 8단계. 파일 저장/불러오기 완성
- [ ] `load_state()`: 파일 없음 → 기본 데이터 / 손상 → 안내 후 기본 데이터로 복구 (try/except)
- [ ] `save_state()`: UTF-8 + `ensure_ascii=False`, 쓰기 오류 try/except
- [ ] 시작 시 "저장된 데이터를 불러왔습니다 (퀴즈 N개, 최고점수 M점)" 표시
- [ ] KeyboardInterrupt/EOFError → 저장 후 안전 종료 마무리
- 커밋 ⑩: `Feat: state.json 저장/불러오기 및 손상 복구 처리`
- 커밋 ⑪: `Fix: Ctrl+C/EOF 발생 시 저장 후 안전 종료 처리`

### 9단계. README 작성
- [ ] 6개 필수 항목 작성: 개요 / 주제 선정 이유 / 실행 방법(`python main.py`) / 기능 목록 / 파일 구조 / state.json 설명(경로·역할·스키마)
- 커밋 ⑫: `Docs: README 작성 (개요/실행법/기능/파일구조/데이터 설명)` → **push**

### 10단계. clone / pull 실습
- [ ] 다른 디렉터리에서 `git clone <repo-url> quiz-game-clone`
- [ ] 클론한 쪽에서 README에 한 줄 추가 → 커밋 ⑬ `Docs: clone 실습 - README 한 줄 추가` → push
- [ ] 원래 작업 디렉터리에서 `git pull` → 변경 반영 확인 (`git log`, README 내용 확인)

### 11단계. 검증 및 제출물 준비
- [ ] **기능 테스트 체크리스트** (아래 5절)
- [ ] 스크린샷 캡처: 개발 환경 / 메뉴 / 퀴즈 추가 / 목록 / 플레이 / 점수 / `git log --oneline --graph`
- [ ] 제출: 저장소 URL + 스크린샷

## 5. 검증 체크리스트 (완료 조건)

**기능**
- [ ] 메뉴 1~5 모두 정상 동작, 5번으로 종료
- [ ] `abc`, `9`, 빈 입력, ` 1 ` (공백 포함) 각각 안내 후 재입력됨
- [ ] 퀴즈 풀기: 정답/오답 표시, 최종 결과 및 점수 표시
- [ ] 퀴즈 추가 → 목록에서 확인 → **재시작 후에도 유지**
- [ ] 최고 점수 갱신 → **재시작 후에도 유지**
- [ ] `state.json` 삭제 후 실행 → 기본 퀴즈 5개로 정상 시작
- [ ] `state.json`을 일부러 깨뜨린 후 실행 → 안내 메시지 + 기본 데이터로 복구
- [ ] 실행 중 Ctrl+C → 안내 메시지 + 저장 + 정상 종료

**Git**
- [ ] 커밋 10개 이상 (계획상 13개), 메시지에 `Feat:`/`Fix:`/`Docs:` 접두어
- [ ] 브랜치 생성 + 병합 이력이 `git log --graph`에 보임
- [ ] 7종 명령어 모두 사용: init ✓ / add ✓ / commit ✓ / push ✓ / checkout ✓(4단계) / clone ✓(10단계) / pull ✓(10단계)

## 6. 보너스 과제 (시간 여유 시, 우선순위 순)

1. **랜덤 출제** — `random.shuffle()` 한 줄 수준, 가성비 최고 (`Feat: 랜덤 출제 추가`)
2. **문제 수 선택** — `read_int` 재사용으로 간단 (`Feat: 풀 문제 수 선택 기능`)
3. **퀴즈 삭제** — 목록 출력 + 번호 입력 재사용 (`Feat: 퀴즈 삭제 기능`)
4. 힌트 기능 / 점수 히스토리 — 스키마 변경이 필요하므로 마지막에
