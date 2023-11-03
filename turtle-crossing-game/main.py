from turtle import Turtle,Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import Car_Manager
import time 

screen=Screen()
screen.bgcolor("white")
screen.setup(width=600,height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

player=Player()
car_manager=Car_Manager()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(player.up_foward,"Up")
screen.onkey(player.down_backword,"Down")
screen.onkey(player.right_way,"Right")
screen.onkey(player.left_way,"Left")


is_game_on=True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_car()
    
    ## arabalara teması altılama 
    for car in car_manager.all_car:
        if car.distance(player)<30:
            is_game_on=False
            scoreboard.game_over()
    
    ##finish cizgisini gecme
    if player.finish_line():
        player.go_start_coor()
        car_manager.level_up()
        scoreboard.increase_point()


###
screen.exitonclick()