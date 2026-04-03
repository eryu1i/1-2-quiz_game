class Quiz:
    def __init__(self, question, choices, answer, hint):
        self.question = question    # 문제 텍스트
        self.choices = choices      # 선택지 (list)
        self.answer = answer        # 정답 (int)
        self.hint = hint            # 힌트

    def display(self):  # 문제와 선택지 출력
        print(f"\n{self.question}\n")
        for i, option in enumerate(self.choices, start=1):
            print(f"  {i}. {option}")

    def check_answer (self, user_answer):
        # 정답 확인 후 True / False 반환
        return self.answer == user_answer

# 기본 퀴즈 데이터
DEFAULT_QUIZZES = [
    Quiz(
        question="텍사스 홀덤에서 각 플레이어에게 처음 주어지는 카드 수는?",
        choices=["1장", "2장", "3장", "4장"],
        answer=2,
        hint="홀덤(hold'em은 hold them이라는 뜻이야)"
    ),
    Quiz(
        question="텍사스 홀덤에서 커뮤니티 카드가 처음 3장 공개되는 단계 이름은?",
        choices=["턴", "리버", "플랍", "프리플랍"],
        answer=3,
        hint="F로 시작해"
    ),
    Quiz(
        question="다음 중 가장 강한 패는?",
        choices=["풀하우스", "포카드", "플러시", "스트레이트"],
        answer=2,
        hint="같은 숫자 4개"
    ),
    Quiz(
        question="블라인드를 먼저 내는 사람은?",
        choices=["딜러", "스몰 블라인드", "빅 블라인드", "UTG"],
        answer=2,
        hint="딜러 바로 왼쪽"
    ),
    Quiz(
        question="텍사스 홀덤에서 커뮤니티 카드는 총 몇 장인가?",
        choices=["3장", "4장", "5장", "6장"],
        answer=3,
        hint="플랍 + 턴 + 리버"
    ),
]