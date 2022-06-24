from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

q = Question

question_bank = []

for question in question_data:
    new_question_text = question["text"]
    new_question_answer = question["answer"]
    new_q = q(new_question_text, new_question_answer)
    question_bank.append(new_q)

b = QuizBrain(question_bank)

while b.stil_have_questions():
    b.next_question()

print(f"You've completed the quiz.\nYour final score is {b.score}/{b.question_number}")
