# main.py

from game import QuizGame


def print_menu(): # 메뉴 출력
    print("\n========================================")
    print("          텍사스 홀덤 퀴즈 게임")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 퀴즈 삭제")
    print("6. 종료")
    print("========================================")

def main():
    game = QuizGame()

    while True:
        try:
            print_menu()
            menu = input("선택: ").strip()

            if menu == "1":     # 퀴즈 풀기
                game.play()

            elif menu == "2":   # 퀴즈 추가
                game.add_quiz()

            elif menu == "3":   # 퀴즈 목록
                game.list_quiz()

            elif menu == "4":   # 점수 확인
                game.show_score()

            elif menu == "5":   # 퀴즈 삭제
                game.delete_quiz()

            elif menu == "6":   # 종료
                print("\n게임을 종료합니다.")
                break

            else:
                print("올바른 번호를 입력하세요.")
                break

        except (KeyboardInterrupt, EOFError):
            print("\n게임을 종료합니다.")
            break

if __name__ == "__main__":
    main()