from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for q_data in question_data:
    question_text = q_data["text"]
    question_answer = q_data["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz ends here....")

