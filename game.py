import random
from quiz import DEFAULT_QUIZZES

class Quizgame:
    def __init__(self):
        self.quizzes = DEFAULT_QUIZZES
        self.best_score = 0

    def play(self):          # 퀴즈 풀기

        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        while True:
            try:
                count = int(input(f"몇 문제 풀까요? (1 ~ {len(self.quizzes)}): ").strip())
                if count < 1 or count > len(self.quizzes):
                    print(f"1 ~ {len(self.quizzes)} 사이의 숫자를 입력하세요.")
                else:
                    break
            except ValueError:
                print("숫자를 입력해주세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n게임을 종료합니다.")
                return

        quizzes = self.quizzes[:]
        random.shuffle(quizzes)
        quizzes = quizzes[:count]

        score = 0

        for i, quiz in enumerate(quizzes, start=1):
            print(f"\n[문제 {i}]")
            quiz.display()

            hint_used = False

            while True:
                try:
                    user_input = input("\n힌트(-0.5점)을 확인하려면 h를 입력하세요.\n정답 입력 : ").strip()

                    if user_input == 'h':
                        print(f"힌트 : {quiz.hint}")
                        hint_used = True
                    else:
                        user_answer = int(user_input)
                        if user_answer < 1 or user_answer > 4:
                            print("1 ~ 4 사이의 숫자를 입력하세요.")
                        else:
                            break
                except ValueError:
                    print("숫자 또는 h를 입력하세요.")
                except (KeyboardInterrupt, EOFError):
                    print("/n게임을 종료합니다.")
                    return
        


    def add_quiz(self):     # 퀴즈 추가
        pass

    def list_quiz(self):    # 퀴즈 목록
        pass

    def show_score(self):   # 점수 확인
        pass

    def delete_quiz(self):  # 퀴즈 삭제
        pass

    def save(self):         # state.json 저장
        pass

    def load(self):         # state.json 불러오기
        pass