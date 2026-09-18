import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.up,key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    for carr in car.all_cars:
        if carr.distance(player) <   20:
            scoreboard.game_over()
            game_is_on = False


    if player.reset_position():
        car.level_up()
        scoreboard.keep_score()

screen.exitonclick()