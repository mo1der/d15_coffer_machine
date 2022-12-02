import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race?\n{colors}\n Enter a color: ")


for t in range(6):
    new_turtle = "turtle" + str(t+1)
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=(-160+(t+1)*50))
    all_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 210:
            winner = turtle.pencolor()
            is_race_on = False

screen.exitonclick()
if winner == user_bet:
    print(f"Good bet on {user_bet}!! You won.")
else:
    print(f"Your lost. Your bet was {user_bet}, but the winner was {winner}. Try next time.")

