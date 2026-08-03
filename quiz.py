"""퀴즈 한 개를 표현하는 Quiz 클래스."""


class Quiz:
    """문제, 선택지 4개, 정답 번호(1~4)를 가지는 퀴즈 한 개."""

    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 사이의 정답 번호

    def display(self, number):
        """문제와 선택지를 화면에 출력한다."""
        print(f"[문제 {number}] {self.question}")
        for i, choice in enumerate(self.choices, start=1):
            print(f"    {i}. {choice}")

    def check(self, user_answer):
        """사용자가 입력한 번호가 정답인지 확인한다."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 저장을 위해 딕셔너리로 변환한다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        """JSON에서 읽은 딕셔너리로 Quiz 인스턴스를 만든다."""
        return cls(
            question=str(data["question"]),
            choices=[str(c) for c in data["choices"]],
            answer=int(data["answer"]),
        )


def default_quizzes():
    """저장 파일이 없을 때 사용하는 기본 퀴즈(영화 주제) 5개."""
    return [
        Quiz(
            "영화 '기생충'으로 아카데미 감독상을 받은 감독은?",
            ["박찬욱", "봉준호", "최동훈", "이창동"],
            2,
        ),
        Quiz(
            "마블 시네마틱 유니버스에서 타노스가 모은 인피니티 스톤의 개수는?",
            ["4개", "5개", "6개", "7개"],
            3,
        ),
        Quiz(
            "영화 '인터스텔라'의 감독은?",
            ["크리스토퍼 놀란", "스티븐 스필버그", "제임스 캐머런", "리들리 스콧"],
            1,
        ),
        Quiz(
            "영화 '올드보이'에서 오대수 역을 맡은 배우는?",
            ["최민식", "송강호", "설경구", "황정민"],
            1,
        ),
        Quiz(
            "한국 영화 최초로 칸 영화제 황금종려상을 받은 작품은?",
            ["올드보이", "기생충", "버닝", "아가씨"],
            2,
        ),
    ]
