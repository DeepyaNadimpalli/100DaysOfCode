from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)  # turning off the animation

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()  # when to refresh or redraw the screen
    time.sleep(0.1)  # delay for 0.1 sec
    snake.move()
screen.exitonclick()
