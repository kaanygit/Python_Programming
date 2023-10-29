# from turtle import Turtle,Screen
# import random

# # turtle objects
# timmy_turtle_objects=Turtle()

# timmy_turtle_objects.shape("square")
# timmy_turtle_objects.color("red")

## CHALLENGE -1 ##
# Way-1
# timmy_turtle_objects.forward(100)
# timmy_turtle_objects.left(90)
# timmy_turtle_objects.forward(100)
# timmy_turtle_objects.left(90)
# timmy_turtle_objects.forward(100)
# timmy_turtle_objects.left(90)
# timmy_turtle_objects.forward(100)
# timmy_turtle_objects.left(90)

# Way-2
# for i in range(4):
#     timmy_turtle_objects.forward(100)
#     timmy_turtle_objects.left(90)
    
# timmy_turtle_objects.color("blue")


## CHALLENGE 2 ##
# for _ in range(15):
#     timmy_turtle_objects.forward(5)
#     timmy_turtle_objects.penup()
#     timmy_turtle_objects.forward(5)
#     timmy_turtle_objects.pendown()


## CHALLENGE 3 ##
# colors = ["white", "yellow", "orange", "red", "green", "blue", "purple", "black"]

# def drawing(num):
#     angle=360/num    
#     for _ in range(num):
#         timmy_turtle_objects.forward(100)
#         timmy_turtle_objects.right(angle)

# for shape_side_in in range(3,11):
#     timmy_turtle_objects.color(random.choice(colors))
#     drawing(shape_side_in)


## CHALLENGE 4 ##
# colors = ["yellow", "orange", "red", "green", "blue", "purple", "black"]
# directions=[0,90,180,270]
# timmy_turtle_objects.pensize(15)
# timmy_turtle_objects.speed("fastest")
# Turtle.colormode(255)

# def randomColorRGB():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     randomColorRGB=(r,g,b)
#     return randomColorRGB

# for _ in range(200):
#     timmy_turtle_objects.color(randomColorRGB())
#     timmy_turtle_objects.forward(30)
#     timmy_turtle_objects.setheading(random.choice(directions))


## CHALLENGE 5 ##
# colors = ["yellow", "orange", "red", "green", "blue", "purple", "black"]

# def randomColor():
#     r=random.randint(0,255)
#     g=random.randint(0,255)
#     b=random.randint(0,255)
#     color=(r,g,b)
#     return color

# timmy_turtle_objects.speed("fastest")
# # timmy_turtle_objects.color(randomColor())
# def draw_sniprograph(size_graph):
#     for _ in range(int(360/size_graph)):
#         timmy_turtle_objects.color(random.choice(colors))
#         timmy_turtle_objects.circle(100)
#         timmy_turtle_objects.setheading(timmy_turtle_objects.heading()+10)
#         timmy_turtle_objects.circle(100)

# draw_sniprograph(5)



## HİRST PAİNTİNG PROJECT ##




#sreens is always open in the bottom 
screen=Screen()
screen.exitonclick()

