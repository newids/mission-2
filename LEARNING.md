# 📚 학습 정리 — 과제 목표를 내 코드로 설명하기

`mission_2.md` 3번 "과제 목표"의 각 항목을 **이 프로젝트의 실제 코드**와 연결해 정리한 문서입니다.
제출 전, 각 항목을 코드를 보지 않고 자기 말로 설명할 수 있는지 점검하세요.

## 1. Python 기초

### 변수가 무엇이고, 왜 사용하는가

값에 이름을 붙여 저장해 두는 공간. 값을 재사용하고 의미를 드러내기 위해 사용한다.

- `quiz_game.py` `play_quiz()`: `total`(문제 수), `correct`(맞힌 수), `score`(점수)를 변수에 담아 채점 결과 계산에 재사용한다.

### `int`, `str`, `bool`, `list`, `dict`의 차이

| 타입 | 의미 | 이 프로젝트에서 |
|---|---|---|
| `int` | 정수 | `Quiz.answer` (정답 번호 1~4), `best_score` |
| `str` | 문자열 | `Quiz.question` (문제 텍스트) |
| `bool` | 참/거짓 | `Quiz.check()`의 반환값 (정답 여부) |
| `list` | 순서 있는 목록 | `Quiz.choices` (선택지 4개), `QuizGame.quizzes` |
| `dict` | 키-값 쌍 | `Quiz.to_dict()`의 반환값, `state.json`을 읽은 결과 |

### `if/elif/else` — 조건 분기

- `quiz_game.py` `run()`: 메뉴 선택 번호(1~5)에 따라 `if choice == 1: ... elif ... else:`로 실행할 기능을 나눈다.
- `play_quiz()`: `if self.best_score is None or score > self.best_score:`로 최고 점수 갱신 여부를 판단한다.

### `for`와 `while`의 차이

- **`for`**: 반복 횟수(대상)가 정해져 있을 때. → `play_quiz()`에서 퀴즈 목록을 순회하며 출제 (`for number, quiz in enumerate(...)`)
- **`while`**: 조건이 만족될 때까지 몇 번일지 모를 때. → `read_int()`에서 올바른 숫자가 들어올 때까지 재입력 (`while True:` + `continue`/`return`), `run()`의 메인 루프

### 함수 정의, 매개변수와 반환값

- `read_int(self, prompt, min_value, max_value)`: 매개변수로 안내 문구와 허용 범위를 받아, 검증된 `int`를 **반환**한다. 메뉴 선택·정답 입력·정답 번호 입력 세 곳에서 재사용 — 같은 검증 코드를 반복하지 않기 위해 함수로 분리했다.

## 2. 클래스와 객체

### 클래스가 무엇이고, 왜 사용하는가

관련된 데이터(속성)와 동작(메서드)을 하나로 묶는 틀. 이 프로젝트는 역할별로 2개 클래스로 분리했다.

- `Quiz` (`quiz.py`): 퀴즈 **한 개**의 데이터(question/choices/answer)와 동작(display/check/직렬화)
- `QuizGame` (`quiz_game.py`): 게임 **전체**의 상태(quizzes/best_score)와 기능(메뉴/풀기/추가/저장)

### `__init__`과 `self`의 역할

- `__init__`: 인스턴스가 만들어질 때 호출되는 초기화 메서드. `Quiz.__init__`은 문제/선택지/정답을 받아 속성에 저장한다.
- `self`: 메서드가 호출된 **그 인스턴스 자신**. `quiz1.check(3)`에서 `self`는 `quiz1`이므로, `self.answer`는 quiz1의 정답을 가리킨다.

### 속성과 메서드 정의/활용

- 속성: `self.question`, `self.choices`, `self.answer` / `self.quizzes`, `self.best_score`
- 메서드: `Quiz.display(number)`(출력), `Quiz.check(user_answer)`(채점), `QuizGame.play_quiz()`(진행) 등 — 기능마다 메서드를 나눠 `run()`은 "메뉴 → 해당 메서드 호출"만 담당한다.

## 3. 파일 입출력

### 파일 열기/읽기/쓰기 기본 과정

`open(경로, 모드, encoding)` → 읽기/쓰기 → 닫기. `with` 문을 쓰면 블록이 끝날 때 자동으로 닫힌다.

- 쓰기: `save_state()` — `with open(temp_file, "w", encoding="utf-8") as f: json.dump(...)`
- 읽기: `load_state()` — `with open(STATE_FILE, "r", encoding="utf-8") as f: json.load(f)`
- (심화) `save_state()`는 임시 파일에 먼저 쓰고 `os.replace()`로 교체한다 — 쓰는 도중 오류가 나도 기존 파일이 깨지지 않게 하기 위해서다.

### JSON이 무엇이고, 왜 데이터 저장에 사용하는가

키-값 구조의 텍스트 데이터 형식. 사람이 읽을 수 있고, Python의 `dict`/`list`와 구조가 1:1로 대응해 `json.dump`/`json.load`만으로 변환된다. 언어에 독립적이라 다른 프로그램과도 호환된다.

- `Quiz.to_dict()`/`Quiz.from_dict()`: 객체 ↔ dict 변환을 클래스가 스스로 담당해, 저장 로직(`QuizGame`)은 JSON 구조를 몰라도 된다.
- 한글 저장을 위해 `encoding="utf-8"` + `ensure_ascii=False`를 사용한다.

### `try/except` 오류 처리

- `load_state()`: `FileNotFoundError`(파일 없음 → 기본 퀴즈), `json.JSONDecodeError` 등(손상 → 안내 후 초기화)을 **예외 종류별로 다르게** 처리한다.
- `save_state()`: `OSError`(디스크 오류), `ValueError`(인코딩 불가 문자)를 잡아 프로그램이 죽지 않게 한다.
- `main.py`: `KeyboardInterrupt`/`EOFError`를 잡아 Ctrl+C에도 저장 후 정상 종료한다.

## 4. Git 기초

### Git이 무엇이고 왜 필요한가

소스 코드의 변경 이력을 스냅샷(커밋) 단위로 기록/관리하는 버전 관리 도구. 언제 무엇을 왜 바꿨는지 추적하고, 이전 상태로 되돌리고, 브랜치로 작업을 분리해 여럿이 협업할 수 있다.

### 7종 명령어 — 이 프로젝트에서 실제로 쓴 순간

| 명령어 | 역할 | 이 프로젝트에서 |
|---|---|---|
| `init` | 저장소 생성 | 프로젝트 시작 시 (`0dba0ec` Initial commit 이전) |
| `add` | 변경을 스테이징 | 매 커밋 전 (기능 단위로 파일 선택) |
| `commit` | 스냅샷 기록 | 기능 단위 17개 커밋 (`Feat:`/`Fix:`/`Docs:` 형식) |
| `push` | 로컬 커밋을 원격에 업로드 | `github.com/newids/mission-2`로 업로드 |
| `pull` | 원격 변경을 로컬로 가져와 병합 | clone 실습에서 push된 `5cefcb2`를 원본 디렉터리로 가져옴 |
| `checkout` | 브랜치 이동/생성 | `feature/play-quiz` 브랜치 생성·이동 |
| `clone` | 원격 저장소 복제 | 별도 디렉터리에 복제해 README 수정 실습 |

### 브랜치 생성과 병합

`git checkout -b feature/play-quiz`로 브랜치를 만들어 퀴즈 풀기 기능을 작업하고, 완성 후 `main`으로 돌아와 `git merge`로 병합했다 (머지 커밋 `bca4d39`). 브랜치 덕분에 기능 개발 중에도 `main`은 항상 동작하는 상태를 유지한다.

### clone과 pull

`clone`으로 원격 저장소 전체(이력 포함)를 새 디렉터리에 복제하고, 그곳에서 커밋·push한 변경(`5cefcb2`)을 기존 작업 디렉터리에서 `pull`로 받아 반영을 확인했다 — 두 명이 협업할 때 일어나는 흐름을 혼자 재현한 것.
