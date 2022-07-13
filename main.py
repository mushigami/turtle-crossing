from turtle import Screen
from pedestrian import Pedestrian
from traffic import Traffic
from scoreboard import Scoreboard
import time


def reset_everything():

    toto.reset_position()
    score_board.reset_scoreboard()
    car_fleet.reset_cars()

def print_key():
    print("Key pressed")


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

toto = Pedestrian()
car_fleet = Traffic()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(toto.move, "Up")
screen.onkeypress(print_key, "Down")


game_is_on = True

while game_is_on:

    # turtle crosses the street
    if toto.ycor() > 250:
        score_board.level_up()
        car_fleet.level_up()
        toto.reset_position()
        time.sleep(0.5)

    # turtle hit by a car
    for car in car_fleet.car_fleet:
        if (toto.distance(car) < 20) and (toto.ycor() > car.ycor() - 10 or toto.ycor() < car.ycor() + 10 ):
            score_board.game_over()
            play_again = screen.textinput("Game Over!", "Play again? [y]es or [n]o ?: ")
            print(play_again)
            if play_again == 'y' or play_again == 'Y':
                print("reset")
                reset_everything()
            else:
                game_is_on = False

    car_fleet.make_cars()
    car_fleet.move_cars()
    car_fleet.remove_cars()
    print(len(car_fleet.car_fleet))

    time.sleep(0.1)
    screen.update()

screen.exitonclick()


