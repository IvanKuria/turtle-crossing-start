import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detects collision with ceiling and returns the player to the start
    # speeds up the cars and increases the level
    if player.ycor() == 280:
        player.origin()
        car_manager.increase_speed()
        scoreboard.increase_score()

    # Detects collision with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 27:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
