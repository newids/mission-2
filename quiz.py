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
