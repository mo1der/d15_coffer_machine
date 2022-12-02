from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.current_score = 0
        self.write_current_score()

    def write_current_score(self):
        self.clear()
        self.write(f"Your current score is: {self.current_score}", False, align="center", font=('Arial', 12, 'bold'))

    def update_score(self):
        self.current_score += 1
        self.write_current_score()

    def game_over(self):
        self.clear()
        self.write(f"GAME OVER. Your final score: {self.current_score}", False, align="center", font=('Arial', 12, 'bold'))


