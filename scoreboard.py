from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.setpos(0, 250)
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Courier", 24, "normal"))
        self.hideturtle()

    def score_up(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Courier", 24, "normal"))



