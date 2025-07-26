import random
color_list=["red","blue","green","yellow","purple","brown","black","pink"]


import turtle
t=turtle.getscreen()
t.bgcolor("light green")
t.title("Turtle")

skk=turtle.Turtle()
skk.shape("turtle")

skk.speed(0.1)
skk.penup()
skk.setposition(0,0)
skk.pendown()


skk.pensize(2)
#skk.circle(50)

skk.pencolor("blue")
for i in range(1000):
    skk.begin_fill()
    skk.forward(i*0.08)
    skk.right(10)#value(angles) in degrees
    skk.end_fill()
    
    color=random.choice(color_list)
    skk.pencolor(color)

turtle.exitonclick()
turtle.done()