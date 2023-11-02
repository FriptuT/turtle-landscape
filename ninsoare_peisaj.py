import turtle

#setup
turtle.setup(width=800, height=600)
# setarea ecranului
wn = turtle.Screen()
wn.bgcolor("lightgreen")

# crearea obiectului turtle
pen = turtle.Turtle()
pen.speed(0)

#setarea culorilor
pen.color("green")
pen.pensize(3) #grosime


# desenarea cerului albastru
pen.fillcolor("skyblue")
pen.begin_fill()
pen.circle(1000)
pen.end_fill()

# desenarea soarelui
pen.penup()
pen.goto(200,250)
pen.pendown()
pen.color("yellow")
pen.begin_fill()
pen.circle(200)
pen.end_fill()

# desenarea norilor
def draw_clouds(x,y,radius):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.color("white")
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

def draw_gray_clouds(x,y,radius,color):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()


draw_gray_clouds(-160,200,50,"gray");
draw_gray_clouds(-60,180,50,"gray");
draw_gray_clouds(30,200,50,"gray");

draw_clouds(-150,220,50)
draw_clouds(-50,200,70)
draw_clouds(20,220,50)


def deseneaza_floare(x,y):
    floare = turtle.Turtle()
    floare.shape("turtle")
    floare.speed(0)
    floare.penup()
    floare.goto(x,y);
    floare.pendown()

    # Desenăm petalele roșii
    floare.color("white")
    for _ in range(36):
        floare.forward(70)
        floare.right(170)

deseneaza_floare(-100,100)
deseneaza_floare(-200,100)
deseneaza_floare(0,130)
deseneaza_floare(-50,70)


def draw_snow(x,y,radius):
    snow = turtle.Turtle()
    snow.shape("circle")
    snow.speed(0)
    snow.penup()
    snow.goto(x,y);
    snow.color("white");
    snow.pendown()
    snow.begin_fill()
    snow.fillcolor("#F0F0F0")
    snow.circle(radius)
    snow.end_fill()

draw_snow(-200,-400,180)
draw_snow(200,-400,180)



turtle.done()