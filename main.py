import turtle as Turtle
import random

screen = Turtle.Screen()

screen.screensize(500, 400)
screen.setup(502, 402)


turtle_colors = ["red", "blue", "green", "orange", "yellow", "purple"]
turtle_y_positions = [-75, -45, -15, 15, 45, 75]
turtles = []


for turtle_index in range(0, 6):
    turtle = Turtle.Turtle(shape="turtle")
    turtle.color(turtle_colors[turtle_index])
    turtle.penup()
    turtle.goto(-230, turtle_y_positions[turtle_index])
    turtles.append(turtle)



player_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a colour: ") 


game_is_running = True

while game_is_running:
    for turtle in turtles:
        turtle.forward(random.randint(1, 10))

        if turtle.xcor() >= 230:
            game_is_running = False
            winning_color = turtle.pencolor()


if player_bet == winning_color:
    print(f"You win! The winning colour was: {winning_color}.")
else:
    print(f"You Lose! The winning colour was: {winning_color}.")


screen.mainloop()