
from game import Game

FILE_PATH = 'state.json'

def main():
    try:
        game = Game(FILE_PATH)

        while True:
            print("\n" + "=" * 40)
            print("My Quiz")
            print("=" * 40)
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("=" * 40)
            selectedNumber = input("번호를 선택하세요:").strip()

            if selectedNumber == '1':
                """퀴즈 풀기"""
                game.play()
            elif selectedNumber == '2':
                """퀴즈 추가"""
                print('test_merge')
            elif selectedNumber == '3':
                """퀴즈 목록"""
                print('3')
            elif selectedNumber == '4':
                """퀴즈 확인"""
                print('4')
            elif selectedNumber == '5':
                """퀴즈 종료"""
                break
            else:
                print("⚠️ 1~5사이의 숫자를 입력하세요.\n")
    except EOFError:
        print("프로그램을 종료합니다.")
    except KeyboardInterrupt:
        print("프로그램을 종료합니다.")


if __name__ == '__main__':
    main()