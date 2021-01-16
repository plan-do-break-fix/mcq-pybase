import hashlib, json
from typing import List


def make_qset(questions: List[dict]) -> dict:
    qset = {}
    for question in [q for q in questions if validate(q)]:
        q_id = hashlib.md5(json.dumps(question).encode()).hexdigest()
        if q_id not in qset.keys():
            qset[q_id] = question
    return qset


def update_qset(qset: dict, questions: List[dict]) -> dict:
    for q in [_q for _q in questions if validate(_q)]:
        q_id = hashlib.md5(json.dumps(q).encode()).hexdigest()
        if q_id not in qset.keys():
            qset[q_id] = q
    return qset


def write_qset(qset: dict, fname: str) -> None:
    with open(f"{fname}.mcquiz", "w") as _f:
        json.dump(qset, _f)


def validate(question: dict) -> bool:
    return True if (question["text"] and
                    question["answers"] and
                    len(question["answers"]) > 1 and
                    sum([a[0] for a in question["answers"]]) > 0
                    ) else False
