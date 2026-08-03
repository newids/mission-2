"""퀴즈 게임 진입점. 실행: python main.py"""

from quiz_game import QuizGame


def main():
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        # Ctrl+C 또는 입력 스트림 종료 시에도 데이터를 저장하고 정상 종료한다.
        print("\n⚠️ 입력이 중단되었습니다. 데이터를 저장하고 종료합니다.")
        game.save_state()


if __name__ == "__main__":
    main()
