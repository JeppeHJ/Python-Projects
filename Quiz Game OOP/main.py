from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for q in question_data:
    question_text = q["question"]
    question_answer = q["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

more_questions = True
quiz = QuizBrain(question_bank)
quiz.next_question()
while quiz.still_has_question():
    quiz.next_question()
else:
    quiz.final_score()