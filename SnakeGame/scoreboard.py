from turtle import Turtle

ALIGN = "center"
FONT = ("Verdana", 15, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 225)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        # self.clear()
        self.goto(0, 0)
        self.color("red")
        self.write(f"Game Over", align=ALIGN, font=FONT)




