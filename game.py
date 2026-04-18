#game.py

import json
import os
from quiz import Quiz


class Game:
    def __init__(self, file_path):
        self.file_path = file_path
        self.quizzes = []
        self.best_score = None
        self.load_quiz()

    def load_quiz(self):
        if not os.path.exists(self.file_path):
              print("저장 파일이 없어 기본 퀴즈를 불러옵니다.")
              self.quizzes = self.get_default_quizzes()
              return
        
        try :        
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.best_score = data.get('best_score', None)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]

            if not self.quizzes:
                print("저장된 퀴즈가 없어 기본 퀴즈를 불러옵니다.")
                self.quizzes = self.get_default_quizzes()

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"파일이 손상되어 기본 퀴즈를 불러옵니다.")
            self.quizzes = self.get_default_quizzes()
            self.best_score = None

    def save_data(self):
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except (IOError, OSError) as e:
            print(f"저장 중 오류 발생: {e}")

    def get_default_quizzes():
        return [
            Quiz(
                question="LCK 팀 T1의 이전 팀명은?",
                choices=["SK Telecom T1", "Samsung T1", "KT T1", "CJ T1"],
                answer=1
            ),
            Quiz(
                question="T1 소속으로 '페이커'라는 닉네임을 사용하는 선수는?",
                choices=["이상혁", "김건부", "허수", "정지훈"],
                answer=1
            ),
            Quiz(
                question="T1이 처음으로 LoL 월드 챔피언십(롤드컵)에서 우승한 해는?",
                choices=["2012", "2013", "2015", "2016"],
                answer=2
            ),
            Quiz(
                question="T1이 2015년 LoL 월드 챔피언십에서 기록한 단일 대회 최소 패배 기록은 몇 패인가?",
                choices=["0패", "1패", "2패", "3패"],
                answer=2
            ),
            Quiz(
                question="T1의 대표적인 팀 컬러는?",
                choices=["파란색", "초록색", "빨간색", "노란색"],
                answer=3
            ),
        ]
    
    def play(self):
        score = 0
        total = len(self.quizzes)
        print(f"\n총 {total}개의 퀴즈가 있습니다.")

        #퀴즈 풀기
        for i, quiz in enumerate(self.quizzes, 1):
            quiz.show_quiz()

            while True:
                try:
                    answer = int(input("정답 입력:").strip())
                    if not answer:
                        print("빈 입력입니다.")
                        continue
                    if answer < 1 or answer > 4:
                        print("1~4 사이의 번호를 입력해주세요.")
                        continue
                    break
                except ValueError:
                    print("숫자를 입력해주세요.")

            if quiz.check_answer(answer):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"오답입니다. 정답은 {quiz.answer}번 입니다.")

        # 결과 출력
        print("\n" + "=" * 40)
        print(f"🏆 결과: {total}문제 중 {score}문제 정답! {score}점")
        if self.best_score < score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = score
        print("=" * 40)

        self.save_data()

