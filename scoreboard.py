from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level_value = 0
        self.color("black")
        self.penup()
        self.goto(-270, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level_value} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.level_value += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)