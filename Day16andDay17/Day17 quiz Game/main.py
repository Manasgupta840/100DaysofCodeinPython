from question_model import Question
from data import question_data
from  quiz_brain import QuizBrain
from prettytable import PrettyTable

d = question_data
question_list = []
for i in question_data:
    text = i["question"]
    answer = i["correct_answer"]
    question = Question(text, answer)
    question_list.append(question)

quiz = QuizBrain(question_list)
while quiz.still_has_question():
    quiz.next_question()

print("_______________________________________________")
print("_______________________________________________")
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
# print(table)
