import turtle
t = turtle.Pen()
t.pen(pencolor="#40BFB0", pensize=5)

t.penup()

#U
t.goto(-200,200)

t.pendown()
t.setheading(270)
t.forward(120)
t.circle(80,180)
t.forward(120)
t.penup()

#n
t.goto(-40,0)
t.setheading(0)
t.forward(20)

t.pendown()
t.setheading(90)
t.forward(60)
t.circle(-40,180)
t.forward(60)
t.penup()

#c
t.goto(60,40)
t.setheading(0)
t.forward(20)

t.forward(80)

t.pendown()
t.setheading(270)
t.circle(-40,180)
t.forward(20)
t.circle(-40,180)
t.penup()

#l
t.goto(160,0)
t.setheading(0)
t.forward(20)

t.forward(20)

t.pendown()
t.setheading(90)
t.forward(200)
t.penup()

#e
t.goto(200,40)
t.setheading(0)
t.forward(20)

t.forward(80)

t.pendown()
t.setheading(270)
t.circle(-40,180)
t.forward(20)
t.circle(-40,180)
t.right(90)
t.forward(80)
t.penup()

