from random import shuffle
from typing import Dict, List


def make_quiz(question_set: Dict,
              length: int,
              shuffle_question_order: bool,
              shuffle_answer_order: bool,
              multichoice_prompts: bool               # Prompts user with number of selections in correct answer
              ) -> List[List]:
    question_ids = list(question_set.keys())
    shuffle(question_ids) if shuffle_question_order else None
    length = len(question_ids) if length == 0 or length > len(question_set.keys()) else length
    questions = [question_set[id] for id in question_ids[:length]]
    questions = [shuffle_answers(question) for question in questions] if shuffle_answer_order else questions
    questions = [add_multichoice_prompts(question) for question in questions] if multichoice_prompts else questions
    return [question_ids, questions]


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
