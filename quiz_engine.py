from random import choice


class QuizEngine:
    '''Runs the quiz.'''

    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions

    def next_question(self):
        '''Displays a random question, and returns the question and user's answer.'''
        # Get a random question
        question = choice(self.questions)

        # Remove it from question bank to prevent it from appearing twice
        self.questions.remove(question)

        self.question_number += 1

        return input(f"\nQ{self.question_number}: {question.text} (True/False)? "), question
