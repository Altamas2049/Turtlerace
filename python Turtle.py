'''from turtle import*
bgcolor("black")
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(100)
    if abs(pos())<2:
        break
end_fill()
done()'''

'''from turtle import*
bgcolor("black")
color('red','green')
while True:
    forward(200)
    left(100)
    circle(60)
    speed(10)
    if abs(pos())<2:
        break
done()'''

'''from turtle import*
bgcolor("black")
pensize(2)
speed(0)

for i in range(6):
    for colour in ["red","green","blue","gray","white","pink"]:
        color(colour)
        circle(100)
        left(10)
hideturtle()'''
        
'''import time
import turtle
from turtle import Turtle
import random
from random import randint

#windows setup

window=turtle.Screen()
window.title("Turtle Race")
turtle.bgcolor("forestgreen")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("Turtle Race",font=("Arial",30,"bold"))
turtle.penup()

#Dirt

turtle.setpos(-400,-180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#finish line

stamp_Size =20
square_size=15
finish_line=200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_Size)
turtle.penup()    
for i in range(10):
    turtle.setpos(finish_line,(150-(i*square_size*2)))
    turtle.stamp()
for j in range(10):
    turtle.setpos(finish_line+square_size,((150-square_size)-(j*square_size*2)))
    turtle.stamp()  
turtle.hideturtle()

# Turtle

turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("black")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250,100)
turtle1.pendown()


# Turtle2

turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("gray")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250,50)
turtle2.pendown()


# Turtle3

turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("white")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250,0)
turtle3.pendown()

# Turtle4

turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("Blue")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250,-50)
turtle4.pendown()

time.sleep(1) #pause the game for 1 sec before starting the race

#Move the Turtle

for i in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))
turtle.exitonclick()'''
