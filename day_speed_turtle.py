from turtle import Turtle, Screen
import random

resolution = [600, 600]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'dark blue', 'purple']
screen = Screen()
screen.setup(resolution[0], resolution[1])
screen.title("ЧерепашкИ")
bet = screen.textinput('Ставка', 'Вибери цвет черепахи, которая победит:')
step = int((resolution[1] - resolution[1] * 0.05) // 6)
startpoint_y = int(-(resolution[1] - resolution[1] * 0.05) // 2)
startpoint_x = int(-(resolution[0] - 20) // 2)
all_turtle = []
race_on = False
win_color = None
end = int(resolution[0] // 2 - 20)



def set_turtle(col: str, x: int, y:int):
    obj = Turtle()
    obj.shape("turtle")
    obj.color(col)
    obj.penup()
    obj.goto(x=x, y=y)
    all_turtle.append(obj)


def speed_for_step(obj: Turtle):
    obj.forward(random.randint(1, 10))


for i in range(len(colors)):
    set_turtle(colors[i], x=startpoint_x, y=startpoint_y)
    startpoint_y += step

if bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        speed_for_step(turtle)
        if turtle.xcor() >= end:
            win_color = turtle.pencolor()
            race_on = False
            break


if win_color == bet:
    print('Перемога!!!')
else:
    print('Ти програв, перемогла =', win_color, 'черепаха')

Screen().exitonclick()
