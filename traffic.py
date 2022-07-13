from turtle import Turtle
import random


CAR_COLORS = ["blue", "red", "orange", "black", "green", "pink", "purple"]
CAR_FLEET_SIZE = 20
CAR_MOVE_SPEED = 10
CAR_SPEED_INCREMENT = 5


class Traffic:
    def __init__(self):
        self.car_fleet = []
        self.car_move_speed = CAR_MOVE_SPEED

    def make_cars(self):
        # Or make a randint between 1-6 and make car when it's a certain value(throwing a dice).
        dice = random.randint(1, 6)
        if dice == 1:
            if len(self.car_fleet) < CAR_FLEET_SIZE:
                new_car = Turtle()
                new_car.shape("square")
                new_car.shapesize(1, 2)
                new_car.color(random.choice(CAR_COLORS))
                new_car.penup()
                new_car.goto(300, random.randint(-220, 220))
                self.car_fleet.append(new_car)

    def move_cars(self):
        for car in self.car_fleet:
            car.goto(car.xcor()-self.car_move_speed, car.ycor())

    def remove_cars(self):
        for car in self.car_fleet:
            if car.xcor() < -320:
                # car.goto(random.randint(300, 1000), random.randint(-220, 220))
                car.clear()
                self.car_fleet.remove(car)

    def reset_cars(self):
        for car in self.car_fleet:
            car.goto(1000, 1000)
            car.clear()
        self.car_fleet = []
        self.car_move_speed = CAR_MOVE_SPEED

    def level_up(self):
        self.car_move_speed += CAR_SPEED_INCREMENT
