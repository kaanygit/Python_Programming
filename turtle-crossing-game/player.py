from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        
    def up_foward(self):
        new_y=self.ycor()+MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
        
    def down_backword(self):
        new_y=self.ycor()-MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
        
    def left_way(self):
        new_x=self.xcor()-MOVE_DISTANCE
        self.goto(new_x,self.ycor())
    
    def right_way(self):
        new_x=self.xcor()+MOVE_DISTANCE
        self.goto(new_x,self.ycor())
        
    def go_start_coor(self):
        self.goto(STARTING_POSITION)
        
    def finish_line(self):
        if (self.ycor()>FINISH_LINE_Y):
            return True
        else:
            return False