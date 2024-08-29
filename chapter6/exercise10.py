from turtle import *
from time import sleep


def Koch(Turtle, lenght, degree):
    if degree == 0:
        Turtle.forward(lenght)
    else:
        length1 = lenght/3
        degree1 = degree - 1 
        Koch(Turtle, length1, degree1)

        Turtle.left(60)
        Koch(Turtle, length1, degree1)

        Turtle.right(120)
        Koch(Turtle, length1, degree1)
        
        Turtle.left(60)
        Koch(Turtle, length1, degree1)


scr = Screen()
scr.bgcolor("light green")
scr.title("Koch")
tur = Turtle()
Koch(tur, 1000, 4)
done()

