from turtle import Turtle, Screen
from random import randint

screen = Screen()  # set up the screen and its background
screen.setup(width=800, height=600)
screen.bgpic('road.gif')

ALIGN = "right"
FONT = ("Courier", 28, "bold")

y_positions = [-260, -172, -85, 2, 85, 172, 260]
colors = ["red", "white", "orange", "blue", "pink", "purple", "yellow"]
all_turtle = []
user_bet = screen.textinput('Enter your bet', prompt='Which turtle (color) will'
                                                     ' win? (red, white, orange'
                                                     ', blue, pink, purple, '
                                                     'yellow)')


for index in range(0, 7):  # create 7 different turtle objects
    new_tur = Turtle(shape="turtle")
    new_tur.shapesize(2)
    new_tur.speed('fastest')
    new_tur.penup()
    new_tur.goto(x=-350, y=y_positions[index])
    new_tur.color(colors[index])
    all_turtle.append(new_tur)

is_on = True

while is_on:  # turtles run with different speeds
    for turtle in all_turtle:
        if turtle.xcor() > 330:  # checks if the turtle crossed the finish line
            is_on = False
            winner = turtle.pencolor().capitalize()
            if winner == user_bet:
                turtle.write(f'You won! {winner} is the winner.',
                             font=FONT, align=ALIGN)
            else:
                turtle.write(f'You lost! {winner} is the winner.',
                             font=FONT, align=ALIGN)
        turtle.forward(randint(0, 20))


screen.exitonclick()  # program stops when screen is clicked
