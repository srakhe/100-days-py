from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def play_game():
    question_bank = []
    for each_question in question_data:
        question_object = Question(each_question['question'], each_question['correct_answer'])
        question_bank.append(question_object)
    brain = QuizBrain(question_bank)
    score = 0
    num_questions_asked = 0
    while brain.still_has_questions():
        print('\n')
        choice = brain.next_question()
        if choice == 'Exit':
            break
        score, num_questions_asked = brain.check_answer(choice)
    print(f'Your final score is {score}/{num_questions_asked}')


play_game()
