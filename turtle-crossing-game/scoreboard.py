from turtle import Turtle
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-200,250)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.score}",align="center",font=FONT)        
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)        
        
    def increase_point(self):
        self.score+=1
        self.update_scoreboard()
