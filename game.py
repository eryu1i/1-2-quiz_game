import json
import random
import datetime
import os
from quiz import DEFAULT_QUIZZES, Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = 0
        self.history = []
        self.load()

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
                print("\n퀴즈 풀기를 취소합니다.")
                return

        quizzes = self.quizzes[:]
        random.shuffle(quizzes)
        quizzes = quizzes[:count]

        score = 0 # 현재 점수
        correct = 0 # 맞춘 문제 수

        for i, quiz in enumerate(quizzes, start=1):
            print(f"\n[문제 {i}]")
            quiz.display()

            hint_used = False

            while True:
                try:
                    user_input = input("\n힌트(사용 시 -0.5점)을 확인하려면 h를 입력하세요.\n정답 입력 : ").strip()

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
                    print("\n퀴즈 풀기를 취소합니다.")
                    return

            if quiz.check_answer(user_answer):
                correct += 1
                if hint_used:
                    print("정답입니다! (힌트 사용 : +0.5점)")
                    score += 0.5
                else:
                    print("정답입니다! (힌트 미사용 : +1점)")
                    score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번 입니다.")

        print("\n========================================")
        print(f"\n{count}문제 중 {correct}문제 정답! ({score}점)")

        if score > self.best_score:
            self.best_score = score
            print("🎉 새로운 최고 점수입니다!")
        else:
            print(f"최고 점수 : {self.best_score}점")
        print("========================================")

        # save history
        self.history.append({
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "count": count,
            "score": score
        })
        self.save()


    def add_quiz(self):     # 퀴즈 추가
        print("\n새로운 퀴즈를 추가합니다.")

        while True:
            try:
                question = input("문제를 입력하세요 : ").strip()
                if question == "":
                    print("문제를 입력해주세요.")
                else:
                    break
            except (KeyboardInterrupt, EOFError):
                print("\n퀴즈 추가를 취소합니다.")
                return

        choices = []
        for i in range(1,5):
            while True:
                try:
                    choice = input(f"선택지 {i} : ").strip()
                    if choice == "":
                        print("선택지를 입력해주세요.")
                    else:
                        choices.append(choice)
                        break
                except (KeyboardInterrupt, EOFError):
                    print("\n퀴즈 추가를 취소합니다.")
                    return

        while True:
            try:
                answer = int(input("정답 번호 (1~4) : ").strip())
                if answer < 1 or answer > 4:
                    print("1 ~ 4 사이의 숫자를 입력하세요.")
                else:
                    break
            except ValueError:
                print("숫자를 입력해주세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n퀴즈 추가를 취소합니다.")
                return

        while True:
            try:
                hint = input("힌트를 입력하세요 : ").strip()
                if hint == "":
                    print("힌트를 입력해주세요.")
                else:
                    break
            except (KeyboardInterrupt, EOFError):
                print("\n퀴즈 추가를 취소합니다.")
                return

        self.quizzes.append(Quiz(question, choices, answer, hint))
        print("\n퀴즈가 추가되었습니다!")
        self.save()

    def list_quiz(self):    # 퀴즈 목록
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("----------------------------------------")
        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"[{i}] {quiz.question}")
        print("----------------------------------------")

    def show_score(self):   # 점수 확인
        if len(self.history) == 0:
            print("아직 퀴즈를 풀지 않았습니다.")
            return

        print(f"\n최고 점수 : {self.best_score}")
        print("\n========================================")
        print("게임 기록")
        print("========================================")
        for record in self.history:
            print(f"{record['date']} | {record['count']}문제 | {record['score']}점")
        print("========================================")

    def delete_quiz(self):  # 퀴즈 삭제
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없습니다.")
            return

        self.list_quiz()

        while True:
            try:
                num = int(input(f"\n삭제할 퀴즈 번호 (1 ~ {len(self.quizzes)}): ").strip())
                if num < 1 or num > len(self.quizzes):
                    print(f"1 ~ {len(self.quizzes)} 사이의 숫자를 입력하세요.")
                else:
                    break
            except ValueError:
                print("숫자를 입력해주세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n퀴즈 삭제를 취소합니다.")
                return

        print(f"\n[{num}] {self.quizzes[num-1].question}")

        while True:
            try:
                confirm = input("정말 삭제하시겠습니까? (y/n): ").strip()
                if confirm == "y":
                    self.quizzes.pop(num-1)
                    print("퀴즈가 삭제되었습니다.")
                    self.save()
                    return
                elif confirm == "n":
                    print("삭제를 취소합니다.")
                    return
                else:
                    print("y 또는 n을 입력하세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n퀴즈 삭제를 취소합니다.")
                return

    def save(self):         # state.json 저장
        if os.path.exists("state.json"):
            os.rename("state.json", "state.json.bak")   # 백업
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer,
                    "hint": quiz.hint
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
            "history": self.history
        }
        try:
            with open("state.json", "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"저장 중 오류가 발생했습니다: {e}")
            if os.path.exists("state.json.bak"):
                os.rename("state.json.bak", "state.json")  # 백업 복구

    def load(self):
        def load_from_file(filepath):  # 파일에서 데이터 읽는 내부 함수
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [
                    Quiz(question=q["question"], choices=q["choices"], answer=q["answer"], hint=q["hint"])
                    for q in data["quizzes"]
                ]
                self.best_score = data.get("best_score", 0)
                self.history = data.get("history", [])

        def use_default():  # 기본 데이터로 초기화하는 내부 함수
            self.quizzes = DEFAULT_QUIZZES
            self.best_score = 0
            self.history = []

        try:
            load_from_file("state.json")
        except FileNotFoundError:
            if os.path.exists("state.json.bak"):
                print("백업 파일에서 복구합니다.")
                try:
                    load_from_file("state.json.bak")
                    os.rename("state.json.bak", "state.json")
                except Exception:
                    print("백업도 손상되었습니다. 기본 데이터로 초기화합니다.")
                    use_default()
            else:
                use_default()
        except Exception:
            print("데이터가 손상되었습니다.")
            if os.path.exists("state.json.bak"):
                print("백업 파일에서 복구합니다.")
                try:
                    load_from_file("state.json.bak")
                    os.rename("state.json.bak", "state.json")
                except Exception:
                    print("백업도 손상되었습니다. 기본 데이터로 초기화합니다.")
                    use_default()
            else:
                print("백업이 없습니다. 기본 데이터로 초기화합니다.")
                use_default()

    def reset(self):
        while True:
            try:
                confirm = input("정말 초기화하시겠습니까? (y/n): ").strip()
                if confirm == "y":
                    if os.path.exists("state.json"):
                        os.remove("state.json")
                    if os.path.exists("state.json.bak"):
                        os.remove("state.json.bak")
                    self.quizzes = DEFAULT_QUIZZES
                    self.best_score = 0
                    self.history = []
                    print("초기화되었습니다.")
                    return
                elif confirm == "n":
                    print("초기화를 취소합니다.")
                    return
                else:
                    print("y 또는 n을 입력하세요.")
            except (KeyboardInterrupt, EOFError):
                print("\n초기화를 취소합니다.")
                return