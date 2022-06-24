class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question_text = self.question_list[self.question_number].text
        question_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question_text} (True/False)?: ")
        self.check_answer(answer, question_answer)

    def stil_have_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, question_answer):
        if answer.lower() == question_answer.lower():
            print("You got it rigth!")
            self.score +=1
        else:
            print(f"That's Wrong. Correct answer was {question_answer}")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
