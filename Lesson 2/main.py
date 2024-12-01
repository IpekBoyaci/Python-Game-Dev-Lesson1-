import pgzrun
from random import randint

#WIDTH and HEIGHT - sys variables - output screen
WIDTH=300
HEIGHT=300

TITLE="Rectangle Pattern"

#draw() - inbuilt function gets called itself .Helps to render animations/shapes/texts...
def draw():
    screen.fill(color="black")

    #rectangel width and height
    width=WIDTH
    height=HEIGHT-200  #300-200=100

    r=255
    g=0
    b=randint(120,255)

    for i in range(20):
        myRect=Rect((0,0),(width,height))
        myRect.center=150,150
        screen.draw.rect(myRect,(r,g,b))

        width=width-10
        height=height+10
        r=r-10
        g=g+10

pgzrun.go()