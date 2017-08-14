import turtle

def drawInfill():
    '''Draw a simple picture using a turtle'''
    turtle.title('Donatello')
    print(turtle.window_height())
    print(turtle.window_width())
    print(turtle.position())
    turtle.penup()
    turtle.setpos(0,-250)
    turtle.begin_fill()
    turtle.left(90)
    turtle.stamp()
    turtle.pendown()
    turtle.color('red')
    turtle.right(90)
    turtle.speed(10)
    turtle.circle(250)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(-250,0)
    turtle.color('black')
    turtle.stamp()
    turtle.penup()
    turtle.setpos(0,250)
    turtle.right(90)
    turtle.stamp()
    turtle.setpos(250,0)
    turtle.right(90)
    turtle.stamp()
    turtle.pendown()


def drawM():
    turtle.penup()
    turtle.setposition(-200,50)
    turtle.right(90)
    turtle.forward(100)
    turtle.pendown()
    turtle.right(180)
    
    turtle.exitonclick()
    
drawInfill()
drawM()

    
