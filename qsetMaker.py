import hashlib, json
from typing import List

def make_qset(questions: List[dict]) -> dict:
    return {hashlib.md5(q["text"].encode()).hexdigest(): q for q in questions if validate(q)}


def update_qset(qset: dict, questions: List[dict]) -> dict:
    for q in [_q for _q in questions if validate(_q)]:
        q_id = hashlib.md5(q["text"].encode()).hexdigest()
        if q_id not in qset.keys():
            qset[q_id] = q
    return qset


def write_qset(qset: dict) -> None:
    pass


def validate(question: dict) -> bool:
    return True if (question["text"] and
                    question["answers"] and
                    len(question["answers"]) > 1 and
                    sum([a[0] for a in question["answers"]]) > 0
                    ) else False
