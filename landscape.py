import turtle

#peisaj munte blocuri case lac copaci

#setup
turtle.setup(width=1000, height = 500)


# Setarea ecranului
wn = turtle.Screen()
wn.bgcolor("lightblue")

# Crearea unui obiect Turtle pentru desenare
pen = turtle.Turtle()
pen.speed(0)  # Setăm viteza maxima

# Setarea culorilor
pen.color("green")
pen.pensize(3)


# Desenarea cerului albastru
pen.fillcolor("skyblue")
pen.begin_fill()
pen.goto(-300, 0)
pen.goto(300, 0)
pen.goto(300, 300)
pen.goto(-300, 300)
pen.end_fill()

# Desenarea soarelui
pen.penup()
pen.goto(200, 200)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# Desenarea munților
pen.penup()
pen.goto(-300, 0)
pen.pendown()
pen.color("gray")
pen.begin_fill()
pen.goto(-100, 200)
pen.goto(0, 100)
pen.goto(100, 200)
pen.goto(300, 0)
pen.goto(-300, 0)
pen.end_fill()

# Desenarea casei
pen.penup()
pen.goto(-200, 0)
pen.pendown()
pen.color("blue")
pen.begin_fill()
pen.goto(-100, 0)
pen.goto(-150, 50)
pen.goto(-200, 0)
pen.end_fill()

# Desenarea blocurilor
pen.penup()
pen.goto(-250, 0)
pen.pendown()
pen.color("brown")
pen.begin_fill()
pen.goto(-250, 100)
pen.goto(-220, 100)
pen.goto(-220, 0)
pen.end_fill()

pen.penup()
pen.goto(-50, 0)
pen.pendown()
pen.color("brown")
pen.begin_fill()
pen.goto(-50, 100)
pen.goto(-20, 100)
pen.goto(-20, 0)
pen.end_fill()

turtle.done()