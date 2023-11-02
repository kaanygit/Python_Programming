##Snake Game

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake-Game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True    
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ## yılanın hareketlendirme
    snake.move()
    
    ## food ile etkilesime girme
    if(snake.head.distance(food)<15):
        food.refresh()
        snake.extend()
        scoreboard.increase()
        
    ## Duvarla etkilesime girmek game over
    if(snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280):
        print("GAME OVER")
        game_is_on=False
        scoreboard.game_over()
        
    ## Kendi kuyruğu ile etkilesime girmek
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()


        


###
screen.exitonclick()

