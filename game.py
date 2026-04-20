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
    
    def run_quiz(self):
        try:
            while True:
                print("\n" + "=" * 40)
                print("🎯 나만의 퀴즈 게임 🎯")
                print("=" * 40)
                print("1. 퀴즈 풀기")
                print("2. 퀴즈 추가")
                print("3. 퀴즈 목록")
                print("4. 점수 확인")
                print("5. 종료")
                print("=" * 40)
                selectedNumber = self.validate_answer("번호를 입력하세요", 5)

                if selectedNumber == 1:
                    """퀴즈 풀기"""
                    self.play_quiz()
                elif selectedNumber == 2:
                    """퀴즈 추가"""
                    self.add_quiz()
                elif selectedNumber == 3:
                    """퀴즈 목록"""
                    self.view_quiz()
                elif selectedNumber == 4:
                    """점수 확인"""
                    self.view_score()
                elif selectedNumber == 5:
                    """퀴즈 종료"""
                    break
        except (EOFError, KeyboardInterrupt):
            print("⚠️ 프로그램을 종료합니다.")

    def load_quiz(self):
        if not os.path.exists(self.file_path):
              print("⚠️ 저장 파일이 없어 기본 퀴즈를 불러옵니다.")
              self.quizzes = self.initialize_quizzes()
              return
        
        try :        
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.best_score = data.get('best_score', None)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]

            if not self.quizzes:
                print("⚠️ 저장된 퀴즈가 없어 기본 퀴즈를 불러옵니다.")
                self.quizzes = self.initialize_quizzes()

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            print(f"⚠️ 파일이 손상되어 기본 퀴즈를 불러옵니다.")
            self.quizzes = self.initialize_quizzes()

    def save_data(self):
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except (IOError, OSError) as e:
            print(f"⚠️ 저장 중 오류 발생: {e}")

    def initialize_quizzes(self):
        self.best_score = None
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
    
    def play_quiz(self):
        new_score = 0
        total = len(self.quizzes)
        print(f"\n총 {total}개의 퀴즈가 있습니다.")

        #퀴즈 풀기
        for i, quiz in enumerate(self.quizzes, 1):
            quiz.show_quiz()

            answer = self.validate_answer()

            if quiz.check_answer(answer):
                print("✅ 정답입니다!")
                new_score += 1
            else:
                print(f"⚠️ 오답입니다. 정답은 {quiz.answer}번 입니다.")

        # 결과 출력
        print("\n" + "=" * 40)
        print(f"🏆 결과: {total}문제 중 {new_score}문제 정답! {new_score}점")
        if self.best_score is None or self.best_score < new_score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = new_score
        print("=" * 40)

        self.save_data()

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        print("-" * 40)

        #문제 입력
        while True:
            question = input("문제를 입력하세요: ").strip()
            if not question:
                print("⚠️ 빈 입력입니다.")
                continue
            break

        #선택지 입력
        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}번을 입력하세요: ").strip()
                if not choice:
                    print("선택지를 입력해주세요.")
                    continue
                choices.append(choice)
                break
        
        answer = self.validate_answer()

        new_quiz = Quiz(question=question, choices=choices, answer=answer)
        self.quizzes.append(new_quiz)
        self.save_data()
        print("✅ 퀴즈가 추가되었습니다!")

    def view_quiz(self):
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for i, quiz in enumerate(self.quizzes, 1):
            print(f"{i} {quiz.question}")
        print("-" * 40)
        
    def view_score(self):
        if self.best_score == None:
            print(f"⚠️ 아직 문제를 풀지 않았습니다.")
        else:
            print(f"🏆 최고 점수: {self.best_score}점")

    def validate_answer(self, comment="정답을 입력하세요", limit=4):
        answer = None
        while True:
            try:
                #입력 앞뒤 공백 제거 후 처리한다
                answer = input(f"{comment}(1~{limit}): ").strip()
                #빈 입력(그냥 Enter)인 경우 안내 메시지 출력 후 재입력 흐름으로 복귀한다.
                if not answer:
                    print("⚠️ 빈 입력입니다.")
                    continue
                answer = int(answer)
                #허용 범위 밖 숫자(예: 메뉴 9, 정답 0) 입력 시 안내 메시지 출력 후 재입력 흐름으로 복귀한다.
                if answer < 1 or answer > limit:
                    print(f"⚠️ 1~{limit} 사이의 번호를 입력해주세요.")
                    continue
                break
            #숫자 변환 실패(예: abc) 시 안내 메시지 출력 후 재입력 흐름으로 복귀한다.
            except ValueError:
                print("⚠️ 숫자를 입력해주세요.")
        return answer

        

