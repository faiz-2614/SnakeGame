from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.scorecard()

    def scorecard(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.write(f"Score : {self.score}    HighScore : {self.high_score}", align="center")

    def increase_score(self):
        self.clear()
        self.score += 1
        self.scorecard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.increase_score()


