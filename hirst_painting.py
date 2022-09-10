import colorgram
from typing import NamedTuple
from turtle import Turtle, Screen
import random

IMAGE_FILENAME = "hirst_painting.jpeg"


def get_colors() -> tuple[NamedTuple]:
    """ "Collects the color palette from the images"""

    palette = colorgram.extract(IMAGE_FILENAME, 30)
    return [color.rgb for color in palette]


def move_pen(pen: Turtle, x: int, y: int) -> None:
    """Moves the pen to an x,y coordinate"""

    current_pendown_state: bool = pen.isdown()
    if pen.isdown():
        pen.up()

    pen.setposition(x, y)

    if current_pendown_state:
        pen.down


def draw_rows(pen: Turtle, palette: tuple[NamedTuple]) -> None:
    pen.down()
    for _ in range(10):
        current_position = pen.position()
        draw_columns(pen, palette)
        pen.setposition(current_position[0], current_position[1] + 50)


def draw_columns(pen: Turtle, palette: tuple[NamedTuple]) -> None:
    for _ in range(10):
        color = random.choice(palette)

        pen.down()
        pen.dot(20, color)
        pen.up()
        pen.forward(50)


def main() -> None:
    pen = Turtle()
    pen.speed("fastest")
    pen.hideturtle()

    screen = Screen()
    screen.colormode(255)

    color_palette = get_colors()

    move_pen(pen, -225, -225)
    draw_rows(pen, color_palette)

    screen.exitonclick()


if __name__ == "__main__":
    main()
