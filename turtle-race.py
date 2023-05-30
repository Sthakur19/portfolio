from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter the color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-100, -50, 0, 50, 100, 150]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color =  turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winer")
            else:
                print(f"You've Lost! The {winning_color} turtle is the winer")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()