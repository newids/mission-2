# ✅ Mission 2 요구사항 체크리스트

`mission_2.md` 요구사항 기준으로 현재 결과물을 검토한 결과입니다. (검토일: 2026-08-04)

## 1. 최종 결과물

### 동작하는 퀴즈 게임

- [x] 메뉴에서 번호 선택 시 기능별 화면 출력 (`quiz_game.py` `run()`)
- [x] 퀴즈 풀기 / 퀴즈 추가 / 퀴즈 목록 / 점수 확인 기능 동작
- [x] 선택 주제(영화) 퀴즈 5개 이상 포함 (`quiz.py` `default_quizzes()` 5개)
- [x] 종료 후 재실행해도 추가한 퀴즈와 최고 점수 유지 (`state.json` 저장/불러오기)

### 코드 구조

- [x] 클래스 2개 이상 정의 (`Quiz`, `QuizGame`)
- [x] 기능별 메서드 분리 (입력: `read_int`/`read_text`, 진행: `play_quiz` 등, 저장: `save_state`/`load_state`)
- [x] 프로젝트 루트 `state.json`에 UTF-8 인코딩으로 저장/불러오기

### GitHub 저장소

- [x] 프로젝트 코드 GitHub 업로드 (`github.com/newids/mission-2`)
- [x] 의미 있는 커밋 10개 이상 (현재 17개, 기능 단위 + `Feat:`/`Fix:`/`Docs:` 형식)
- [x] 브랜치 생성 및 병합 1회 이상 (`feature/play-quiz` → `main` 병합, 커밋 `bca4d39`)
- [x] `clone`/`pull` 각 1회 이상 사용 (clone 실습 커밋 `5cefcb2` → 원본 디렉터리에서 pull)
- [x] README.md 필수 항목 6종 (개요 / 주제 선정 이유 / 실행 방법 / 기능 목록 / 파일 구조 / 데이터 파일 설명)

## 2. 기능 요구사항 (4번 항목)

- [x] 1. Git 저장소 설정 (`.gitignore`, `README.md`, 첫 commit/push)
- [x] 2. 메뉴 기능 (출력, 선택, 종료, 잘못된 입력 처리)
- [x] 3. 공통 입력/예외 처리
  - [x] 공백 제거 / 숫자 변환 실패 / 범위 밖 / 빈 입력 → 안내 후 재입력 (`read_int`)
  - [x] `Ctrl+C`(KeyboardInterrupt) / EOF → 저장 후 안전 종료 (`main.py`)
  - [x] 데이터 파일 없음 → 기본 퀴즈 사용, 손상 → 안내 후 기본 데이터로 복구 (`load_state`)
  - [x] (추가) 터미널 인코딩 불일치로 깨진 문자 입력 → 안내 후 재입력, 저장 실패 시에도 기존 파일 보존
- [x] 4. `Quiz` 클래스 (question/choices/answer 속성, 출력/정답 확인 메서드)
- [x] 5. 기본 퀴즈 데이터 (영화 주제 5개, `Quiz` 인스턴스로 생성)
- [x] 6. 퀴즈 풀기 (브랜치 작업 후 병합, 출제/채점/결과, 퀴즈 없음 처리)
- [x] 7. 퀴즈 추가 (입력 검증, 파일 저장)
- [x] 8. 퀴즈 목록 (없는 경우 처리)
- [x] 9. 점수 확인 (최고 점수 비교/갱신/저장, 기록 없음 처리)
- [x] 10. `QuizGame` 클래스 (퀴즈 목록/최고 점수 속성, 기능별 메서드)
- [x] 11. 파일 저장/불러오기 (`state.json`, UTF-8, try/except, 스키마 일관성)
- [x] 12. README.md 작성
- [x] 13. clone/pull 실습

## 3. 제약 사항

- [x] Python 3.10 이상, 외부 라이브러리 없이 표준 라이브러리만 사용
- [x] 기능별 함수 분리, 클래스 2개 이상
- [x] Git 기초 명령어 7종 사용 (`init`, `add`, `commit`, `push`, `pull`, `checkout`, `clone`)

## 4. 보너스 과제 (선택)

- [x] 랜덤 출제 (`random.sample`, 커밋 `334f359`)
- [ ] 문제 수 선택
- [ ] 힌트 기능
- [ ] 퀴즈 삭제 기능
- [ ] 점수 기록 히스토리

## 5. 제출 전 남은 작업 (직접 수행 필요)

- [ ] **스크린샷 캡처** → `docs/screenshots/`에 저장 (안내: [docs/screenshots/README.md](docs/screenshots/README.md))
  - [ ] 개발 환경 설정 (VSCode, Python 버전, Git 설정)
  - [ ] 실행 결과: 퀴즈 추가 / 목록 / 플레이 / 점수 (`menu.png`, `play.png`, `add_quiz.png`, `score.png`)
  - [ ] `git log --oneline --graph` 결과
- [ ] **`state.json` 정리**: 테스트용 퀴즈("문제"/"답1~4")를 제출 전에 삭제할지 결정
- [ ] **GitHub 푸시**: 최근 커밋들을 `git push`로 반영 (인증 필요)
- [ ] 제출: GitHub 저장소 URL + 스크린샷

## 6. 과제 목표 (설명 능력) 점검

미션 3번 "과제 목표"는 코드가 아니라 **스스로 설명할 수 있는지**가 기준입니다.
각 항목을 이 프로젝트의 실제 코드와 연결해 정리한 [LEARNING.md](LEARNING.md)를 보고 셀프 점검하세요.

- [ ] Python 기초 (변수, 자료형, 조건문, 반복문, 함수)를 설명할 수 있다
- [ ] 클래스와 객체 (`__init__`, `self`, 속성/메서드)를 설명할 수 있다
- [ ] 파일 입출력 (open/JSON/try-except)을 설명할 수 있다
- [ ] Git 기초 (7종 명령어, 브랜치 생성/병합, clone/pull)를 설명할 수 있다
