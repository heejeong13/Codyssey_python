import json
from pathlib import Path

def main():
    while True:
        print("=============")
        print("My Quiz")
        print("=============")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=============")
        selectedNumber = input("번호를 선택하세요:").strip()

        if selectedNumber == '1':
            BASE_DIR = Path(__file__).resolve().parent
            STATE_FILE_PATH = BASE_DIR/"data"/'state.json'
            print(STATE_FILE_PATH)

            with open(STATE_FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                high_score = data.get('best_score',0)
                quizzes = data.get('quizzes',[])
                for quiz in quizzes:
                    print(quiz)
                    print(quiz["question"])
        elif selectedNumber == '2':
            print('2')
        elif selectedNumber == '3':
            print('3')
        elif selectedNumber == '4':
            print('4')
        elif selectedNumber == '5':
            print('5')
            break
        else:
            print("!!!!! 1~5사이의 숫자를 입력하세요. !!!!!\n")

if __name__ == '__main__':
    main()