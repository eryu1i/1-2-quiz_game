# main.py

def print_menu(): # 메뉴 출력
    pass

def main():
    while True:
        try:
            print_menu()
            menu = input("선택: ").strip()

            if menu == "1":     # 퀴즈 풀기
                pass

            elif menu == "2":   # 퀴즈 추가
                pass

            elif menu == "3":   # 퀴즈 목록
                pass

            elif menu == "4":   # 점수 확인
                pass

            elif menu == "5":   # 퀴즈 삭제
                pass

            elif menu == "6":   # 종료
                break

            else:
                print("올바른 번호를 입력하세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n게임을 종료합니다.")
            break
                # Ctrl + C, 입력 스트림 종료 처리

if __name__ == "__main__":
    main()