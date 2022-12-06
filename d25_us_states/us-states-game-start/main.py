import turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()



# game_is_on = True
#
# while game_is_on:
#     user_answer = input("What's another state name?")
#
# screen.exitonclick()
