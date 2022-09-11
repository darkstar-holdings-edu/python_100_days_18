from turtle import Turtle, Screen
import random

pen = Turtle()
pen.speed("fastest")
screen = Screen()
screen.colormode(255)


def get_color() -> tuple[int]:
    return (random.randint(0, 255) for _ in range(3))


def draw_square():
    pen.home()

    for _ in range(4):
        pen.forward(100)
        pen.right(90)


def draw_dotted_line():
    pen.home()

    for _ in range(25):
        pen.forward(10)
        pen.up()
        pen.forward(10)
        pen.down()


def draw_shapes():
    pen.home()

    def draw_shape(sides: int) -> None:
        angle = 360 / sides
        for _ in range(sides):
            pen.forward(100)
            pen.right(angle)

    for sides in range(3, 11):
        rgb = [random.randint(0, 255) for _ in range(3)]
        pen.pencolor(rgb)
        draw_shape(sides)


def random_walk():
    WALK_DISTANCE = 30

    pen.home()
    pen.width(15)

    def draw_left(pen):
        pen.left(90)
        pen.forward(WALK_DISTANCE)

    def draw_right(pen):
        pen.right(90)
        pen.forward(WALK_DISTANCE)

    def draw_forward(pen):
        pen.forward(WALK_DISTANCE)

    def draw_backward(pen):
        pen.backward(WALK_DISTANCE)

    for _ in range(300):
        direction = random.choice(
            [
                lambda pen: draw_forward(pen),
                lambda pen: draw_backward(pen),
                lambda pen: draw_left(pen),
                lambda pen: draw_right(pen),
            ]
        )

        rgb = (random.randint(0, 255) for _ in range(3))
        pen.pencolor(rgb)
        direction(pen)


def spirograph():
    pen.home()

    for _ in range(36):
        pen.pencolor(get_color())
        pen.circle(100)
        pen.left(10)


# draw_square()
# draw_dotted_line()
# draw_shapes()
# random_walk()
spirograph()

foo = sorted(pen.pen().items())[3][1]
print(foo)
screen.exitonclick()
