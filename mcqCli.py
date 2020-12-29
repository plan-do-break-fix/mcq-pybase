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
            response = self.keyed_response(len(q["answers"]), self.parse_answer(input()))
            self.review(response, q["answers"])
            self.current += 1

    def parse_answer(self, answer: str):
        """Returns a list of selected answer choice indices."""
        labels = list(set([label.upper() for label in answer if label.upper() in "ABCDEF"]))
        labels.sort()
        return [self.lookup[label] for label in labels]

    def keyed_response(self, choice_count, selections):
        response = [0 for i in range(choice_count)]
        for i in selections:
            response[i] = 1
        return response

    def review(self, response, answers):
        if response == [a[0] for a in answers]:
            print("Correct.")
        else:
            for i in range(len(answers)):
                if answers[i][0]:
                    if response[i]:
                        print(f"{self.reverse_lookup[i]} is correct.")
                    else:
                        print(f"{self.reverse_lookup[i]} should have been selected.")
                elif not answers[i][0] and response[i]:
                    print(f"{self.reverse_lookup[i]} is not correct.")
