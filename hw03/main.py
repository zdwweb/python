from turtle import *
from math import *


def rectangle():
    #  绘制旗面
    color('red', 'red')
    speed(8)
    penup()
    goto(-500, -300)
    #  自定义原点
    pendown()
    begin_fill()
    for i in range(2):
        forward(960)
        left(90)
        forward(640)
        left(90)
    end_fill()
    
    
def draw_star(radius, star_x, star_y):
    #  以五等分圆法绘制五角星
    color('yellow', 'yellow')
    speed(8)
    goto(star_x, star_y)
    pt = []
    pt.append(pos())
    i = 0
    while i < 4:
        circle(radius, 72)
        pt.append(pos())
        i+= 1
    circle(radius,72)
    begin_fill()
    goto(pt[0])
    pendown()
    for i in [3,1,4,2,0]:
        goto(pt[i])
    end_fill()
def find_small_star(angle,star_center):
    #  找到副星的起始位置并画出五角星
    penup()
    setheading(0)
    goto(-340,180)
    left(angle)
    goto(star_center)
    backward(32)
    right(90)
    draw_star(32,xcor(),ycor())
def find_big_star():
    #  找到主星的起始位置并画出五角星
    penup()
    setheading(0)
    goto(-340,180)
    left(90)
    forward(32*3)
    left(90)
    draw_star(32*3,xcor(),ycor())
def main():
    rectangle()
    find_big_star()
    find_small_star(atan(3/5)*180/pi,(-180,276))
    find_small_star(atan(1/7)*180/pi,(-116,212))
    find_small_star(-atan(2/7)*180/pi,(-116,116))
    find_small_star(-atan(4/5)*180/pi,(-180,52))
    hideturtle()
    done()
    
    
main()
