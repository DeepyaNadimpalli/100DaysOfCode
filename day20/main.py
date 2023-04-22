from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake game")
screen.tracer(0)  # turning off the animation

snake = Snake()
food = Food()
score = Score()

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
    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.refresh()
        snake.extend()
        score.increase_score()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        print("collision with wall")
        score.game_over()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            print("collision with tail")
            score.game_over()
screen.exitonclick()
