import turtle

#solar sistem

pen = turtle.Turtle()
#setup
turtle.setup(width=1000, height = 500)

# Setarea ecranului
wn = turtle.Screen()
wn.bgcolor("black")

pen.speed(0)

#desenarea soarelui
pen.penup()         # Ridică penița pentru a preveni desenarea
pen.goto(600,-250)
pen.pendown()
pen.color("orange")
pen.pensize(25)
pen.fillcolor("yellow")
pen.begin_fill()
pen.circle(300)

pen.end_fill()


def draw_orange_circles(x, y, radius):
    hole = turtle.Turtle()
    hole.speed(0)
    hole.color("orange")
    hole.penup()
    hole.goto(x, y)
    hole.pendown()

    hole.begin_fill()
    hole.circle(radius)
    hole.end_fill()


def draw_red_circles(x, y, radius):
    hole = turtle.Turtle()
    hole.speed(0)
    hole.color("red")
    hole.penup()
    hole.goto(x, y)
    hole.pendown()

    hole.begin_fill()
    hole.circle(radius)
    hole.end_fill()

draw_orange_circles(400,-100,10)
draw_orange_circles(350,-50,30)
draw_orange_circles(415,50,25)
draw_orange_circles(430, 120,30)
draw_orange_circles(450,-100,30)
draw_orange_circles(450,-150,20)
draw_orange_circles(400,-100,10)

draw_red_circles(400,-100,10)
draw_red_circles(350,-10,3)
draw_red_circles(330,-20,2)
draw_red_circles(380,-20,2)

draw_red_circles(415,60,3)
draw_red_circles(425,40,3)

draw_red_circles(430, 140,4)
draw_red_circles(420, 130,3)
draw_red_circles(440, 150,3)


draw_red_circles(450,-80,10)
draw_red_circles(430,-90,4)
draw_red_circles(410,-100,5)


# functie pentru desenarea planetei mercury
def draw_mercury(x, y, radius):
    hole = turtle.Turtle()
    hole.speed(0)
    hole.color("white")
    hole.penup()
    hole.goto(x, y)
    hole.pendown()
    hole.fillcolor("gray")

    hole.begin_fill()
    hole.circle(radius)
    hole.end_fill()

def draw_black_circles(x, y, radius):
    hole = turtle.Turtle()
    hole.speed(0)
    hole.color("black")
    hole.penup()
    hole.goto(x, y)
    hole.pendown()

    hole.begin_fill()
    hole.circle(radius)
    hole.end_fill()

draw_mercury(190,-50,70)

draw_black_circles(190,-40,10)
draw_black_circles(200,0,9)
draw_black_circles(150,40,10)
draw_black_circles(220,40,9)

# functie pentru desenarea planetei venus
def draw_venus(x, y, radius):
    hole = turtle.Turtle()
    hole.speed(0)
    hole.color("white")
    hole.penup()
    hole.goto(x, y)
    hole.pendown()
    hole.fillcolor("#F6F6A8")
    hole.begin_fill()
    hole.circle(radius)
    hole.end_fill()

draw_venus(-55,-95,130)


def draw_terra(x, y, radius):
    hole = turtle.Turtle()
    hole.speed(0)
    hole.color("white")
    hole.penup()
    hole.goto(x, y)
    hole.pendown()
    hole.fillcolor("#5186FF")
    hole.begin_fill()
    hole.circle(radius)
    hole.end_fill()

draw_terra(-350,-80,110)

def draw_green_circles(x, y, radius):
    hole = turtle.Turtle()
    hole.speed(0)
    hole.color("green")
    hole.penup()
    hole.goto(x, y)
    hole.pendown()

    hole.begin_fill()
    hole.circle(radius)
    hole.end_fill()

def draw_white_circles(x, y, radius):
    hole = turtle.Turtle()
    hole.speed(0)
    hole.color("white")
    hole.penup()
    hole.goto(x, y)
    hole.pendown()

    hole.begin_fill()
    hole.circle(radius)
    hole.end_fill()

def draw_brown_circles(x, y, radius):
    hole = turtle.Turtle()
    hole.speed(0)
    hole.color("brown")
    hole.penup()
    hole.goto(x, y)
    hole.pendown()

    hole.begin_fill()
    hole.circle(radius)
    hole.end_fill()

turtle.done()  # Așteaptă până când utilizatorul închide fereastra
