from turtle import Turtle
import pandas


class CheckState(Turtle):

    def __init__(self, user_type):
        super().__init__()
        self.location = None
        self.new_state = None
        self.good_answer = False
        self.user_answer = user_type
        self.data_file = pandas.read_csv('50_states.csv')
        self.states_data = pandas.DataFrame(self.data_file)
        # self.check_answer()

    def write_state(self, loc):
        self.new_state = Turtle()
        self.new_state.penup()
        self.new_state.color("black")
        self.new_state.hideturtle()
        self.location = loc
        self.new_state.goto(self.location)
        self.new_state.write(f"{self.user_answer}", align="center", font=("Verdana", 12, "normal"))

    def check_answer(self):
        self.good_answer = False
        if self.user_answer in self.states_data['state'].values:
            answer_state_x = int(self.states_data[self.states_data['state'] == self.user_answer]["x"])
            answer_state_y = int(self.states_data[self.states_data['state'] == self.user_answer]["y"])
            location = (answer_state_x, answer_state_y)
            self.write_state(location)
            self.good_answer = True
            return self.good_answer





        


# state_on_map = turtle.Turtle
# state_on_map.hideturtle()
# state_on_map.color("black")
# state_on_map.penup()
# state_on_map.goto(add_loc)
# state_on_map.write(f"{answer_state}", align="center", font=("Verdana", 12, "normal"))

