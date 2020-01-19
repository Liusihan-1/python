#题目：画图，学用rectangle画方形
import turtle

turtle.setup(width=0.5, height=0.5, startx=None, starty=None)
turtle.hideturtle()
turtle.pensize(3)
turtle.pencolor('red')
turtle.speed(3)
turtle.penup()
turtle.goto(-150, 75)
turtle.pendown()
turtle.forward(300)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(150)
turtle.done()
