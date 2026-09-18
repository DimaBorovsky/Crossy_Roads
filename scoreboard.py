from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("black")
        self.goto(-240,260)
        self.score = 0
        self.write(f" Level: {self.score}", align="center", font=FONT)


    def keep_score(self):
        self.clear()
        self.score += 1
        self.write(f" Level: {self.score}",align="center",font=FONT)


    def game_over(self):
        self.clear()
        self.home()
        self.write(f" GAME OVER !", align="center", font=FONT)