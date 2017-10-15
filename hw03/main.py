import turtle as t
from math import *

# Self defining origin.
origin_x, origin_y = -500, -300


def rectangle(length, width):
    t.color('red', 'red')
    t.speed(10)
    t.penup()
    t.goto(origin_x, origin_y)
    t.pendown()
    t.begin_fill()
    for counter in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.end_fill()


def draw_star(radius, star_x, star_y):
    #  Draw the pentagonal star by the five equal division
    t.color('yellow', 'yellow')
    t.speed(10)
    t.goto(star_x, star_y)
    pt = []
    pt.append(t.pos())
    for counter in range(4):
        t.circle(radius, 72)
        pt.append(t.pos())
    t.circle(radius, 72)
    t.begin_fill()
    t.goto(pt[0])
    t.pendown()
    for i in [3, 1, 4, 2, 0]:
        t.goto(pt[i])
    t.end_fill()


def find_star(angle, radius, star_center=None):
    #  Locate the starting position and draw the star.
    t.penup()
    t.setheading(0)
    t.goto(big_star_center)
    if angle == 90:#  Position the big star.
        t.left(90)
        t.forward(radius)
        t.left(90)
    else:          #  Position the little star.
        t.left(angle)
        t.goto(star_center)
        t.backward(radius)
        t.right(90)
    draw_star(radius, t.xcor(), t.ycor())


def main():
    length, width = 960, 640
    small_radius = 32
    big_radius = small_radius * 3
    unit = width / 20
    # Base on the external contact of the star.
    base_x, base_y = origin_x, origin_y + unit * 10
    global big_star_center
    big_star_center = (base_x + unit * 5, base_y + unit * 5)
    rectangle(length, width)
    find_star(90, big_radius)
    find_star(atan(3 / 5) * 180 / pi, small_radius,
              (base_x + unit * 10, base_y + unit * 8))
    find_star(atan(1 / 7) * 180 / pi, small_radius,
              (base_x + unit * 12, base_y + unit * 6))
    find_star(-atan(2 / 7) * 180 / pi, small_radius,
              (base_x + unit * 12, base_y + unit * 3))
    find_star(-atan(4 / 5) * 180 / pi, small_radius,
              (base_x + unit * 10, base_y + unit * 1))
    t.hideturtle()
    t.done()


main()
