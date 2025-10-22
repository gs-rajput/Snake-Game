from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard
sc = Screen()
food = Food()
score = Scoreboard()
sc.setup(width=600, height=600)
sc.title("The Snake Game")
sc.bgcolor("black")
sc.tracer(0)
snake = Snake()
sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.left, "Left")
sc.onkey(snake.right, "Right")


game_on = True
while game_on:
    sc.update()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_update()

    #detect collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.create()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.create()




sc.exitonclick()