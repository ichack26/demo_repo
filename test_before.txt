# demo.py

from typing import List


def clamp(value, lo, hi):
    return max(lo, min(value, hi))


def average(xs: List[int]):
    if not xs:
        return 0
    return sum(xs) / len(xs)


class Logger:
    def __init__(self):
        self.messages = []

    def log(self, msg):
        self.messages.append(msg)

    def dump(self):
        for m in self.messages:
            print(m)


class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def is_adult(self):
        return self.age >= 18


class ScoreEngine:
    class Weights:
        BASE = 10
        AGE = 2

    def __init__(self, logger: Logger):
        self.logger = logger

    def compute_score(self, user: User, values: List[int]):
        self.logger.log(f"Computing score for {user.name}")

        def normalize(xs):
            return [clamp(x, 0, 100) for x in xs]

        vals = normalize(values)
        avg = average(vals)

        score = self.Weights.BASE + avg * self.Weights.AGE

        if user.is_adult():
            score += 5

        return int(score)


class ReportBuilder:
    def __init__(self, engine: ScoreEngine):
        self.engine = engine

    def build_report(self, user: User, values: List[int]):
        score = self.engine.compute_score(user, values)

        status = self._status_from_score(score)

        return {
            "name": user.name,
            "score": score,
            "status": status,
        }

    def _status_from_score(self, score):
        if score > 200:
            return "excellent"
        elif score > 100:
            return "good"
        else:
            return "average"


def run_pipeline(name, age, values):
    logger = Logger()
    engine = ScoreEngine(logger)
    builder = ReportBuilder(engine)

    user = User(name, age)

    report = builder.build_report(user, values)

    logger.dump()
    return report


def main():
    data = [120, 50, -10, 80]
    report = run_pipeline("Alice", 20, data)
    print(report)


if __name__ == "__main__":
    main()