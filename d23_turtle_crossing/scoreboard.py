from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.hideturtle()
        self.goto(-220, 250)
        self.write_current_level()

    def write_current_level(self):
        self.clear()
        self.write(f"Level: {self.current_level}", False, align="center", font=FONT)

    def update_level(self):
        self.current_level += 1
        self.write_current_level()



