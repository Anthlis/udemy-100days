from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, car_speed):
        super().__init__()
        self.color(choice(COLORS))
        self.shape("square")
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.moving_distance = car_speed
        self.goto(280, randint(-250, 250))

    def move_car(self):
        self.forward(self.moving_distance)




class CarManager:
    def __init__(self) -> None:
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()


    def create_car(self):
        car = Car(self.car_speed)
        self.all_cars.append(car)

    def move_all(self):
        for car in self.all_cars:
            car.move_car()
            
    def level_up(self):
        for car in self.all_cars:
            car.moving_distance += MOVE_INCREMENT

        self.car_speed += MOVE_INCREMENT

