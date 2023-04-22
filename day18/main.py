# import colorgram
# colors = colorgram.extract('painting.jpg', 25)
# rgb_colors_list = []
# for i in range(len(colors)):
#     rgb_colors_list.append(((colors[i].rgb)[0], (colors[i].rgb)[1], (colors[i].rgb)[2]))
# print(rgb_colors_list)
# rgb_colors_list = rgb_colors_list[2:]
color_list = [(222, 163, 66), (19, 45, 87), (136, 61, 84), (177, 60, 44), (239, 230, 223), (126, 40, 61), (21, 86, 61),
              (59, 48, 37), (250, 194, 42), (13, 117, 146), (57, 146, 72), (229, 86, 36), (231, 172, 190), (57, 71, 39),
              (197, 102, 134), (197, 125, 150), (156, 191, 185), (30, 67, 58), (236, 245, 241), (166, 204, 202),
              (62, 26, 45), (145, 165, 181), (6, 79, 111)]
import turtle as t
import random

t.colormode(255)
my_turtle = t.Turtle()
my_turtle.speed("fastest")
my_turtle.seth(225)
my_turtle.penup()
my_turtle.forward(250)
my_turtle.seth(0)
my_turtle.hideturtle()
for i in range(10):
    for j in range(10):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.forward(50)

    my_turtle.left(90)
    my_turtle.forward(50)
    my_turtle.left(90)
    my_turtle.forward(500)
    my_turtle.right(180)

screen = t.Screen()
screen.exitonclick()
