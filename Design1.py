import turtle
import threading
import time

# create object of turtle
pen = turtle.Turtle()

# background
pen.getscreen()
turtle.screensize(1980, 1080, "black")

# pen color
pen.color("purple")

# pen speed
pen.speed(10)


# method to draw
def draw():
    for x in range(50, 80, 2):
        pen.circle(x)



time.sleep(5)
# for loop to call circles
for i in range(10):
    threading.Timer(5, draw)
    draw()
    pen.left(36)

turtle.done()
