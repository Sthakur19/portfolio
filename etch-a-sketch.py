from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def counterclockwise():
    tim.right(45)

def clockwise():
    tim.left(45)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(counterclockwise, "a")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

screen.setup()
screen.exitonclick()