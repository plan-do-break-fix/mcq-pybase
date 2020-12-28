from random import shuffle
from typing import Dict, List


def make_quiz(question_set: List[Dict],
              length: int,
              shuffle_question_order: bool,
              shuffle_answer_order: bool,
              multichoice_prompts: bool               # Prompts user with number of selections in correct answer
              ) -> List[Dict]:
    shuffle(question_set) if shuffle_question_order else None
    qset = question_set if length == 0 else question_set[:length]
    qset = [shuffle_answers(q) for q in qset] if shuffle_answer_order else qset
    qset = [add_multichoice_prompts(q) for q in qset] if multichoice_prompts else qset
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
