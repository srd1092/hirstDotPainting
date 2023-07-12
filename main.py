import colorgram
import turtle as t
import random

rgb_colors = []
extracted_colors = colorgram.extract("colors_sample.jpg", 45)
for color in extracted_colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

my_turtle = t.Turtle()
t.colormode(255)
my_turtle.speed("fastest")
my_turtle.penup()
my_turtle.hideturtle()


y_value = -220

for _ in range(10):
    my_turtle.setx(-220)
    my_turtle.sety(y_value)
    y_value += 50
    for _ in range(10):
        my_turtle.dot(20, random.choice(rgb_colors))
        my_turtle.forward(50)

screen = t.Screen()
screen.exitonclick()

