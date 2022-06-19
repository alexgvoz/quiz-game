from data import question_data
from question_model import Question

class QuizBrain:

    def __init__(self):
        self.question_list = []
        self.question_number = 0
        self.score = 0

        for i in range(len(question_data)):
            self.question_list.append(Question(question_data[i]["question"], question_data[i]["correct_answer"]))

    def start(self):
        while self.question_number < len(self.question_list):
            self.askQuestion()

        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}")

    def askQuestion(self):
        cur_question = self.question_list[self.question_number]
        user_input = input(f"Q.{self.question_number + 1}: {cur_question.text} (True/False)?: ")
        self.question_number += 1
        self.checkAnswer(user_input, cur_question.answer)

    def checkAnswer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, wrong answer.")

        print(f"Score: {self.score}/{self.question_number}\n")
