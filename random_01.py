import turtle
import random

turtle.penup()

#List of colors
colors = ["red", "green", "blue", "yellow", "orange", "black", "purple"]

for i in range(20):
    #innitialize range of randoem number
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    #set the random position
    turtle.setposition(x,y)
    #set random colors
    i = random.randint(0, len(colors)-1)

    turtle.dot(colors[i])

turtle.exitonclick()
