from game_data import question_data
from question import Question
from quiz_engine import QuizEngine
from os import system

question_bank = [Question(dic['text'], dic['answer']) for dic in question_data]
quiz_engine = QuizEngine(question_bank)

art = """
 
  _____     _       _      _____         _    
 |_   _| __(_)_   _(_) __ |_   _| __ ___| | __
   | || '__| \ \ / / |/ _` || || '__/ _ \ |/ /
   | || |  | |\ V /| | (_| || || | |  __/   < 
   |_||_|  |_| \_/ |_|\__,_||_||_|  \___|_|\_\
                                              

"""


def run_quiz():
    '''Contains the game loop.'''

    score = 0
    is_correct = True

    while is_correct and quiz_engine.questions:
        system("clear")
        print(art)

        if score > 0:
            print("\nCorrect" + str("!" * score))

        print(f"Your score: {score}")
        user_ans, question = quiz_engine.next_question()

        if user_ans.title() != question.answer:
            is_correct = False
        else:
            score += 1

    system("clear")
    print(f"Final score: {score}")

    if not is_correct:
        print("\nWrong answer!\n")
    else:
        print("\nWell done! All questions answered correctly.\n")


run_quiz()
