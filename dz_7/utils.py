import random

from question import Question
from data import questions_data


def load_question():
    questions = []

    for question_data in questions_data:
        questions.append(Question(
            question_data["q"],
            int(question_data["d"]),
            question_data["a"]
        ))
    random.shuffle(questions)
    return questions


def count_correct_answer(questions):
    correct_counter = 0

    for question in questions:
        if question.is_correct():
            correct_counter += 1
    return correct_counter


def count_points(questions):
    points_counter = 0

    for question in questions:
        if question.is_correct():
            points_counter += question.get_points()
    return points_counter
