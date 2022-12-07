import turtle
import pandas
import add_states

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)

good_answers = []
game_is_on = True

while game_is_on:
    user_answer = ((screen.textinput(title=f"Guess the State Game. Score is {len(good_answers)}/50.", prompt="What's another state name?                                           ")).lower()).title()
    add_states.CheckState(user_answer)
    if (add_states.CheckState(user_answer).check_answer() == True) and (user_answer not in good_answers):
        good_answers.append(user_answer)
        print(good_answers)
    if user_answer == "Exit":
        break

data_file = pandas.read_csv('50_states.csv')
states_list = data_file.state.to_list()

for state in good_answers:
    states_list.remove(state)

states_to_learning = pandas.DataFrame(states_list)
states_to_learning.to_csv("statest_to_learn.csv")




# turtle.mainloop()

# print(states_data["state"][2:5])
# print(states_data)

#
# screen.exitonclick()
