"""
Simple CLI quiz app
"""
import make


class Sprint:

    def __init__(self, question_set):
        self.lookup = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}
        self.reverse_lookup = {0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F"}
        self.current = 1
        self.questions = make.make_quiz(question_set, 20, True, True, True)

    def quiz_loop(self):
        while self.current <= len(self.questions):
            q = self.questions[self.current - 1]
            print(q["text"])
            for count, answer in enumerate(q["answers"]):
                print(f"{self.reverse_lookup[count - 1]}. {answer[1]}")
            resp = self.parse_answer(input())
            self.current += 1

    def parse_answer(self, answer: str):
        """Returns a list of selected answer choice indices."""
        labels = list(set([label.upper() for label in answer if label.upper() in "ABCDEF"]))
        return [self.lookup[label] for label in labels]
