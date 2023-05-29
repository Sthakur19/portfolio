from turtle import Turtle, Screen
import random


tim = Turtle()
screen = Screen()

def color_random():
    red = random.random()
    green = random.random()
    blue = random.random()
    color = (red, green, blue)
    return color


# draw a shape e.g triangle, ractangle etc

# def draw_shape(num_of_side):
#     angle = 360 / num_of_side
#     for _ in range(num_of_side):
#         tim.forward(100)
#         tim.right(angle)
# for num_of_side in range(3, 11):
#     tim.color(color_random())
#     draw_shape(num_of_side)

# Randaom walk

# directions = [0, 90, 180, 270]
# tim.width(5)
# tim.speed('slow')
# for _ in range(200):
#     tim.color(color_random())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# draw Spirograph

def draw_spinograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(color_random())
        tim.circle(50)
        tim.setheading(tim.heading() + size_of_gap)

draw_spinograph(5)

screen.setup(width=500, height=500)
screen.exitonclick()  

