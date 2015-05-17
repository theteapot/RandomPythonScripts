import turtle

def draw_diamond(squirtle):
    squirtle.left(20)
    squirtle.forward(70)
    squirtle.right(40)
    squirtle.forward(70)
    squirtle.right(140)
    squirtle.forward(70)
    squirtle.right(40)
    squirtle.forward(70)


def draw_art():
    # window points to an object of type Screen.
    # window.bgcolor sets the background color of the window.
    window = turtle.Screen()
    window.bgcolor("white")

    # turt points to an object of type Turtle.
    turt = turtle.Turtle()
    turt.speed(0)
    turt.color("blue")
    turt.shape("turtle")
    # Call draw diamond 90 times, and have turt start with a difference of 4 degrees
    # NB: the range and difference in degrees must be multiples of 360, eg. 90 * 40 = 360 degrees.
    for num in range(0, 90):
        draw_diamond(turt)
        turt.right(156)

    # Finish off drawing with a straight vertical downward line.
    turt.right(90)
    turt.forward(250)

    # will close the window when user clicks on it (provided the drawing has finished).
    window.exitonclick()

draw_art()
