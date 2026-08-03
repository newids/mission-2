"""게임 전체를 관리하는 QuizGame 클래스."""


class QuizGame:
    """메뉴를 보여주고 사용자가 선택한 기능을 실행하는 게임 관리 클래스."""

    def __init__(self):
        self.quizzes = []
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

    def run(self):
        """메인 루프: 메뉴 출력 → 번호 선택 → 기능 실행."""
        while True:
            self.show_menu()
            raw = input("    선택: ").strip()
            if not raw.isdigit() or not 1 <= int(raw) <= 5:
                print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                continue
            choice = int(raw)
            if choice == 1:
                print("(준비 중) 퀴즈 풀기")
            elif choice == 2:
                print("(준비 중) 퀴즈 추가")
            elif choice == 3:
                print("(준비 중) 퀴즈 목록")
            elif choice == 4:
                print("(준비 중) 점수 확인")
            else:
                print("👋 게임을 종료합니다.")
                break
