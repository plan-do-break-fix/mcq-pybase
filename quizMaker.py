from random import shuffle
from typing import Dict, List


def make_quiz(question_set: Dict,
              length: int,
              shuffle_question_order: bool,
              shuffle_answer_order: bool,
              multichoice_prompts: bool               # Prompts user with number of selections in correct answer
              ) -> Dict:
    questions = list(question_set.keys())
    shuffle(questions) if shuffle_question_order else None
    length = len(question_set.keys()) if length == 0 or length < len(question_set.keys()) else length
    qset = {question: question_set[question] for question in questions[:length]}
    qset = {question: shuffle_answers(qset[question]) for question in qset} if shuffle_answer_order else qset
    qset = {question: add_multichoice_prompts(qset[question]) for question in qset} if multichoice_prompts else qset
    return qset


def shuffle_answers(question: dict) -> dict:
    """Randomize answer order for all questions in question set."""
    shuffle(question["answers"])
    return question


def add_multichoice_prompts(question: dict) -> dict:
    """Add a prompt to questions with more than one correct answer selection."""
    if correct_choices(question) > 1:
        question["text"] += f" [Select {correct_choices(question)}]"
    return question


def correct_choices(question: dict) -> int:
    """Return the number of correct answer selection for question."""
    return sum(a[0] for a in question["answers"])
