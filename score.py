from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(arg=f'Score: {self.score}', move=False, align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.write(arg="Game Over...", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update()
