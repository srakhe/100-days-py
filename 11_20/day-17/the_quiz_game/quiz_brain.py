import random


class QuizBrain:
    def __init__(self, list):
        self.question_number = 0
        self.questions_list = list
        self.score = 0
        self.done_list = [0]

    def already_done(self, number):
        if number in self.done_list:
            return True
        else:
            self.done_list.append(number)
            return False

    def next_question(self):
        question = self.questions_list[self.question_number]
        choice = input(f'Q. {question.text} True or False? [Enter "exit" to give up]').title()
        return choice

    def still_has_questions(self):
        return len(self.done_list) < len(self.questions_list)

    def check_answer(self, choice):
        question = self.questions_list[self.question_number]
        if choice == question.answer:
            self.score += 1
            print(f'Answer is Correct! Your current score= {self.score}')
        else:
            print(f'Answer is Incorrect! Your current score= {self.score}')
        while self.already_done(self.question_number):
            self.question_number = random.randint(0, len(self.questions_list) - 1)
        return self.score, len(self.done_list)
