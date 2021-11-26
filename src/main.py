import turtle
from turtle import *
import random

prazno = []

#skrin
sc = turtle.Screen()
sc.setup(600, 600)
sc.bgcolor("black")

#rezultat
score = turtle.Turtle()
score.hideturtle()
score.color("white")
score.penup()
score.goto(-200, 150)

#možic
mozic = turtle.Turtle()
mozic.hideturtle()
mozic.color("white")
mozic.shape()




beseda = textinput("Pozor", "vnesi")
for i in beseda:
    prazno.append("_")
score.write(" ".join(prazno), font= ["courier", 25])
poizkus = len(beseda)*3

zgresen = 0
while True:

    sc.update()





    for i in range(len(beseda)*3):
        crka = textinput("Pozor", "Vnesi crko")

        score.undo()
        poizkus -= 1
        for j in range(len(beseda)):
            if beseda[j] == crka:
                prazno[j] = crka
                nova_beseda = " ".join(prazno)
                continue
            elif beseda[j] != crka or crka == prazno[j]:

                 nova_beseda = " ".join(prazno)
            
        if crka not in beseda:
            zgresen += 1




        if zgresen == 1:
            mozic.penup()
            mozic.goto(-70, -100)
            mozic.pendown()
            mozic.forward(140)
        if zgresen == 2:
            mozic.penup()
            mozic.goto(0, -100)
            mozic.pendown()
            mozic.setheading(90)
            mozic.forward(175)
            mozic.setheading(0)
        if zgresen == 3:
            mozic.penup()
            mozic.goto(0, 75)
            mozic.pendown()
            mozic.forward(125)
        if zgresen == 4:
            mozic.penup()
            mozic.goto(125, 75)
            mozic.pendown()
            mozic.setheading(270)
            mozic.forward(50)
        if zgresen == 5:
            mozic.penup()
            mozic.goto(105, 5)
            mozic.pendown()
            mozic.circle(20)
        if zgresen == 6:
            mozic.penup()
            mozic.goto(125, -16)
            mozic.pendown()
            mozic.setheading(270)
            mozic.forward(50)
        if zgresen == 7:
            mozic.penup()
            mozic.goto(125, -30)
            mozic.pendown()
            mozic.setheading(45)
            mozic.forward(40)
        if zgresen == 8:
            mozic.penup()
            mozic.goto(125, -30)
            mozic.pendown()
            mozic.setheading(135)
            mozic.forward(40)
        if zgresen == 9:
            mozic.penup()
            mozic.goto(125, -65)
            mozic.pendown()
            mozic.setheading(225)
            mozic.forward(50)
        if zgresen == 10:
            mozic.penup()
            mozic.goto(125, -65)
            mozic.pendown()
            mozic.setheading(315)
            mozic.forward(50)







        score.write(nova_beseda, font= ["courier", 25])

    if poizkus == 0:
        break