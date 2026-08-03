"""게임 전체를 관리하는 QuizGame 클래스."""

import json

from quiz import Quiz, default_quizzes

STATE_FILE = "state.json"


class QuizGame:
    """메뉴를 보여주고 사용자가 선택한 기능을 실행하는 게임 관리 클래스."""

    def __init__(self):
        self.quizzes = default_quizzes()
        self.best_score = None  # 아직 퀴즈를 풀지 않았으면 None

    def show_menu(self):
        print()
        print("=" * 40)
        print("          🎯 나만의 퀴즈 게임 🎯")
        print("=" * 40)
        print("        1. 퀴즈 풀기")
        print("        2. 퀴즈 추가")
        print("        3. 퀴즈 목록")
        print("        4. 점수 확인")
        print("        5. 종료")
        print("=" * 40)

    def read_int(self, prompt, min_value, max_value):
        """숫자 입력 공통 처리: 공백 제거, 빈 입력/숫자 아님/범위 밖이면 재입력."""
        while True:
            raw = input(prompt).strip()
            if raw == "":
                print(f"⚠️ 아무것도 입력되지 않았습니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue
            try:
                value = int(raw)
            except ValueError:
                print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue
            if not min_value <= value <= max_value:
                print(f"⚠️ 잘못된 입력입니다. {min_value}-{max_value} 사이의 숫자를 입력하세요.")
                continue
            return value

    def read_text(self, prompt):
        """문자 입력 공통 처리: 공백 제거, 빈 입력이면 재입력."""
        while True:
            raw = input(prompt).strip()
            if raw:
                return raw
            print("⚠️ 빈 입력은 사용할 수 없습니다. 다시 입력하세요.")

    def play_quiz(self):
        """저장된 퀴즈를 순서대로 출제하고 채점한 뒤 결과를 표시한다."""
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가하세요.")
            return

        total = len(self.quizzes)
        correct = 0
        print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            quiz.display(number)
            user_answer = self.read_int("    정답 입력: ", 1, 4)
            if quiz.check(user_answer):
                correct += 1
                print("✅ 정답입니다!")
            else:
                print(f"❌ 오답입니다! (정답: {quiz.answer}. {quiz.choices[quiz.answer - 1]})")
            print("-" * 40)

        score = round(correct / total * 100)
        print("=" * 40)
        print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        self.save_state()
        print("=" * 40)

    def show_score(self):
        """최고 점수를 출력한다. 아직 퀴즈를 풀지 않았으면 안내한다."""
        if self.best_score is None:
            print("⚠️ 아직 퀴즈를 푼 기록이 없습니다. 먼저 퀴즈를 풀어보세요!")
            return
        print(f"\n🏆 최고 점수: {self.best_score}점")

    def add_quiz(self):
        """문제/선택지 4개/정답 번호를 입력받아 새 퀴즈를 등록하고 저장한다."""
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = self.read_text("문제를 입력하세요: ")
        choices = []
        for i in range(1, 5):
            choices.append(self.read_text(f"선택지 {i}: "))
        answer = self.read_int("정답 번호 (1-4): ", 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print("\n✅ 퀴즈가 추가되었습니다!")

    def list_quizzes(self):
        """등록된 퀴즈 목록을 번호와 함께 출력한다."""
        if not self.quizzes:
            print("⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for number, quiz in enumerate(self.quizzes, start=1):
            print(f"[{number}] {quiz.question}")
        print("-" * 40)

    def save_state(self):
        """퀴즈 목록과 최고 점수를 state.json에 UTF-8로 저장한다."""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError as e:
            print(f"⚠️ 데이터 저장에 실패했습니다: {e}")

    def load_state(self):
        """state.json에서 데이터를 불러온다. 없거나 손상되면 기본 퀴즈를 사용한다."""
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.quizzes = [Quiz.from_dict(q) for q in data["quizzes"]]
            self.best_score = data.get("best_score")
            best = f"{self.best_score}점" if self.best_score is not None else "없음"
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {best})")
        except FileNotFoundError:
            print("📂 저장된 데이터가 없어 기본 퀴즈로 시작합니다.")
        except (json.JSONDecodeError, KeyError, TypeError, ValueError, OSError):
            self.quizzes = default_quizzes()
            self.best_score = None
            print("⚠️ 데이터 파일이 손상되어 기본 퀴즈로 초기화합니다.")
            self.save_state()

    def run(self):
        """메인 루프: 메뉴 출력 → 번호 선택 → 기능 실행."""
        self.load_state()
        while True:
            self.show_menu()
            choice = self.read_int("    선택: ", 1, 5)
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            else:
                self.save_state()
                print("👋 게임을 종료합니다.")
                break
