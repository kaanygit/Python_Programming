from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question["question"]
    question_answer=question["correct_answer"]
    new_question=Question(q_text=question_text,q_answer=question_answer)
    question_bank.append(new_question)
    
quiz=QuizBrain(question_bank)    
quiz.next_question()


while quiz.still_has_questions():
    quiz.next_question()

print("Quiz Tamamlandı")
print(f"Final Skorunuz {quiz.score}/{len(quiz.question_list)}")
print("\n")


# print(question_bank[0].text)
# print(question_bank[0].answer)