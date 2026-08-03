"""게임 전체를 관리하는 QuizGame 클래스."""

from quiz import default_quizzes


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
        print("=" * 40)

    def run(self):
        """메인 루프: 메뉴 출력 → 번호 선택 → 기능 실행."""
        while True:
            self.show_menu()
            choice = self.read_int("    선택: ", 1, 5)
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                print("(준비 중) 퀴즈 추가")
            elif choice == 3:
                print("(준비 중) 퀴즈 목록")
            elif choice == 4:
                print("(준비 중) 점수 확인")
            else:
                print("👋 게임을 종료합니다.")
                break
