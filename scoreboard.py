from turtle import Turtle
ALIGNMENT = "center"
FONT = ("arial", 13, "normal")
SBPOSTION = (0, 280)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.setposition(SBPOSTION)
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write("Game over...", False, align= ALIGNMENT, font=FONT)

    def new_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)