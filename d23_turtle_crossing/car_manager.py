import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.possible_cars_roads = []
        self.car_speed = STARTING_MOVE_DISTANCE
        for y_road in range(-250, 250, 25):
            self.possible_cars_roads.append(y_road)
        # self.roads_taken = []

        # self.roads_taken.sort()

    def add_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        search_for_free_road = True
        # while search_for_free_road:
        new_road = random.choice(self.possible_cars_roads)
            # if new_road not in self.roads_taken:
            #     search_for_free_road = False
        new_car.goto(300, new_road)
        # self.roads_taken.append(new_road)
        self.cars.append(new_car)

    def go_left(self):
        # for car in range(0, len(self.cars)):
        for car in self.cars:
            # new_x = self.cars[car].xcor() - STARTING_MOVE_DISTANCE
            # self.cars[car].goto(new_x, self.cars[car].ycor())
            car.goto(car.xcor()-self.car_speed, car.ycor())

        for car in self.cars:
            if car.xcor() <= -300:
                car.hideturtle()
                # print("TAK")
                # self.roads_taken.remove(car.ycor())
                self.cars.remove(car)
            # else:
                # print(f"NIE {car.xcor()}")

        # print(f" wszystkie samochody {self.cars}")
        # print(f" zajęte drogi {self.roads_taken}")

    def level_up(self):
        self.car_speed += MOVE_INCREMENT