from turtle import Turtle, Screen
import random
import colorgram

tim = Turtle()
tim.shape("circle")
tim.turtlesize(2, 2, None)
tim.turtlesize(2, 2, None)

colors = []
colors_set = colorgram.extract('picture_spots.png', 50)
for nr in range(len(colors_set)):
    rgb_color = colors_set[nr].rgb
    red = rgb_color.r
    green = rgb_color.g
    blue = rgb_color.b
    added_color = (red, green, blue)
    colors.append(added_color)


def select_color():
    return random.choice(colors)


# for number in range(3, 11):

def draw_shape(walls_number):
    tim.pencolor(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    tim.pensize(walls_number-2)
    for _ in range(walls_number):
        tim.forward(100)
        tim.right(360/walls_number)
    return
def draw_shapes(n_shapes):
    for n in range (3,n_shapes+3):
        draw_shape(n)
def random_color():
    rc = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    return rc
def random_walk(how_long):
    tim.pensize(7)
    possible_angles = [0, 90, 180, 270]
    tim.hideturtle()
    for nr in range(how_long):
        # tim.speed(round(10*nr/how_long,10))
        tim.speed(6)
        tim.pencolor(random_color())
        tim.setheading(random.choice(possible_angles))
        tim.forward(40)

# random_walk(100)
# tim.hideturtle()
# tim.speed("fastest")
#
# for _ in range (100):
#     tim.circle(100)
#     tim.setheading(tim.heading()+10)
#     tim.pencolor(random_color())
#     if tim.heading() == 0:
#         break


def draw_circle():
    tim.hideturtle()
    tim.speed(1)
    for i in range (360):
        tim.forward(1)
        tim.right(1)


screen = Screen()
screen.screensize(300, 300)
screen.bgcolor("grey")
screen.colormode(255)

tim.up()

tim.pencolor(select_color())

tim.color(select_color())
tim.setposition(-500, 400)

for aa in range(1, 6):
    for _ in range(6):
        tim.stamp()
        tim.forward(200)
        tim.color(select_color())
    tim.setposition(-500, 400-200*aa)


screen.exitonclick()

