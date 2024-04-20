import turtle
import random

tom = turtle.Turtle()
tom.hideturtle()
tom.up()
tom.goto(0, -180)
screen = turtle.Screen()
screen.setup(width=500, height=500)


def outline():
    """
    Draws an outline of 500 x 500 for the purpose of user reference incase if they play game in maximized window.
    this line will help him to check out the range or area of the game.
    """
    outline_obj = turtle.Turtle()
    outline_obj.up()
    outline_obj.speed(0)
    outline_obj.hideturtle()
    outline_obj.pensize(3)
    outline_obj.goto(x=-250, y=250)
    outline_obj.down()

    # draw an outline Border for game.
    for _ in range(4):
        outline_obj.forward(500)
        outline_obj.right(90)


def draw_court():
    """
    This function will draw out the racing lines between the turtle and also the ending or a winning line,
    which helps to display the give separate block for each of the turtle.
    """
    y_line = -187.50
    x_line = -200
    lining = turtle.Turtle()
    lining.hideturtle()
    lining.penup()
    lining.pensize(5)
    lining.pencolor("light grey")
    lining.speed(0)
    lining.goto(x=x_line, y=y_line)

    # draw the line between the turtle
    for _ in range(6):
        lining.pendown()
        lining.forward(360)
        lining.penup()
        y_line += 75
        lining.goto(x=x_line, y=y_line)

    # draw out the winning final line
    lining.goto(x=200, y=lining.ycor() - 35)
    lining.pencolor('black')
    lining.right(90)
    for _ in range(20):
        lining.pendown()
        lining.forward(10)
        lining.penup()
        lining.forward(13)


def print_turtle(winner):
    screen.clear()
    t = turtle.Turtle("turtle")
    t.up()
    t.color(winner)
    t.goto(x=0, y=120)
    t.left(90)
    t.turtlesize(6, 6, 0)


def check_guess(guess, color, winner):
    """
    This will take three parameters.
    guess -> which the user guess the winning turtle
    color -> this will be the list of the turtle colors
    winner -> get which turtle won the race

    after these parameters it will check and give its decision about user guess
    """
    if guess.capitalize() in color:
        if guess.capitalize() == winner:
            print_turtle(winner)
            tom.write("WOW!! You guessed it correct, congrats", align="center", font=("Arial", 16, "normal"))
        else:
            print_turtle(winner)
            tom.write("AH! Wrong guess, Bad luck", align="center", font=("Arial", 16, "normal"))

    else:
        screen.clear()
        tom.write("You bet on wrong candidate", align="center", font=("Arial", 16, "normal"))


def game_starts():
    """
    Every thing is this game will be start from here itself this will create turtle objects.
    It asks user to make a bet on any of the turtle which will win.
    check out that the
    """
    x = -230
    y = -150
    reached = False
    tommy = turtle.Turtle()
    tommy.hideturtle()
    turtles = []
    turtle_color = ['Red', 'Blue', 'Green', 'Orange', 'Pink']
    outline()
    draw_court()

    for value in range(5):
        turtle_obj = turtle.Turtle("turtle")
        turtle_obj.speed(6)
        turtle_obj.up()
        turtle_obj.color(turtle_color[value])
        turtle_obj.goto(x=x, y=y)
        y += 75
        turtles.append(turtle_obj)

    guess_color = screen.textinput(title="Who will win", prompt="Enter the turtle color which you guess?")
    while not reached:
        if guess_color is not None:
            for obj in turtles:
                obj.forward(random.randint(0, 10))
                # Check if any turtle passed the final line
                if round(obj.xcor()) >= 200:
                    won_turtle_color = obj.pencolor()
                    # Checks if the Guess color is correct or not
                    check_guess(guess=guess_color, color=turtle_color, winner=won_turtle_color)
                    reached = True
                    break

        else:
            screen.clear()
            tommy.up()
            tommy.left(90)
            tommy.forward(50)
            tommy.turtlesize(8, 8, 0)
            tommy.showturtle()
            reached = True
            tom.write("You must make a guess, click to exit.", align="center", font=("Arial", 16, "normal"))


game_end = False
while not game_end:
    you_play = screen.textinput(title='Yes or No', prompt='Will you play now') == ('yes' or 's')
    if you_play:
        screen.clear()
        game_starts()
    else:
        screen.clear()
        st = turtle.Turtle()
        st.up()
        st.left(90)

        st.forward(50)
        st.turtlesize(8, 8, 0)
        tom.write("Okay, click to exit.", align='center', font=("Arial", 16, "normal"))
        game_end = True
screen.exitonclick()
