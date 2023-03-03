# Jet-Fighter
A fun fighter game. ✈️
Download everything from the google drive below:
https://drive.google.com/drive/folders/1pk1dcVRwkt_UVM8gd-Ud_YW9X7a0SEVT

#Jet Fighter
import turtle
from turtle import *
import math
from math import tan

# Functions

#this function uses the turtle.listen() function and tells the
#game what to do when a button is pressed. It also moves the planes forward
def movement():
    jet.forward(FORWARD_SPEED)
    fighter.forward(FORWARD_SPEED)
    ata_jet_follow()
    ata_jet_seek()
    ata_fighter_follow()
    ata_fighter_seek()
    
    turtle.onkey(jet_left,"Left")
    turtle.onkey(jet_right,"Right")
    turtle.onkey(jet_forward,"Up")
    turtle.onkey(jet_shoot,"Down")
    jet_bullet_follow()
    turtle.onkey(ataj_activator,"/")
    
    turtle.onkey(fighter_left,"a")
    turtle.onkey(fighter_right,"d")
    turtle.onkey(fighter_forward,"w")
    turtle.onkey(fighter_shoot,"s")
    turtle.onkey(ataf_activator,"e")
    
    turtle.onkey(pause, "space")
    turtle.onkey(Quit, "Q")
    
    borders_of_jet()
    borders_of_fighter()

#this function occurs when the left arrow key is pressed.
#it takes no parameters but uses two global variables, jet turning
#angle and ltd. It subtracts frum the jet turning angle
def jet_left():
    global jetturningangle, jltd, jrtd
    jltd = jltd+1
    if jltd == 1 and jetturningangle == 0:

        jetturningangle = 11
    if jetturningangle == 0:
        jetturningangle = 11
    else:
        jetturningangle = jetturningangle-1
        
    jet.left(HEADING_STEP)
    turtle.addshape(name=jetturn[jetturningangle], shape=None) 
    jet.shape(jetturn[jetturningangle])
    jrtd = jrtd+1


#This functions occurs when the right arrow key is pressed. It has
#no parameters but uses the global variable jet turning angle
#It adds to jet turning angle and turns the plane right 30 degrees
def jet_right():
    global jetturningangle, jrtd, jltd
    jrtd = jrtd+1
    if jetturningangle == 0 and jrtd == 1:
        jetturningangle = 0
    if jetturningangle <= 11 and jrtd !=1:
        jetturningangle = jetturningangle+1
    if jetturningangle == 12:
        jetturningangle = 0
    jet.right(HEADING_STEP)
    turtle.addshape(name=jetturn[jetturningangle], shape=None) 
    jet.shape(jetturn[jetturningangle])
    jltd = jltd +1

#this function serves as a kind of boost when the up arrow key is pressed.
#it moves the jet forward 1.5 times the forward speed
def jet_forward():
    jet.forward(1.5*FORWARD_SPEED)

def jet_shoot():
    jbullets.append(Turtle())
    last_bullet = jbullets[len(jbullets)-1]
    last_bullet.setheading(jet.heading())
    last_bullet.pu()
    last_bullet.shape('circle')
    last_bullet.shapesize(.1,.1,.1)
    last_bullet.goto(jet.xcor(),jet.ycor())

def jet_bullet_follow():
    for turt in jbullets:
        turt.pu()
        if turt.xcor()> 600 or turt.xcor()< -600:
            turt.goto(600,0)
            mover = 0
        elif turt.ycor()> 600 or turt.ycor()< -600:
            turt.goto(600,0)
            mover = 0
        else:
            mover = 2
        turt.forward(FORWARD_SPEED*mover)
        
def fighter_right():
    global fighterturningangle, frtd, fltd
    frtd = frtd+1
    if frtd == 1 and fighterturningangle == 0:
        fighterturningangle = 11
    if fighterturningangle == 0:
        fighterturningangle = 11
    else:
        fighterturningangle = fighterturningangle-1
        
    fighter.right(HEADING_STEP)
    turtle.addshape(name=fighterturn[fighterturningangle], shape=None) 
    fighter.shape(fighterturn[fighterturningangle])
    fltd = fltd+1

def fighter_left():
    global fighterturningangle, fltd, frtd
    fltd = fltd+1
    if fighterturningangle == 0 and fltd == 1:
        fighterturningangle = 0
    if fighterturningangle <= 11 and fltd != 1:
        fighterturningangle = fighterturningangle+1
    if fighterturningangle == 12:
        fighterturningangle = 0
    fighter.left(HEADING_STEP)
    turtle.addshape(name=fighterturn[fighterturningangle], shape=None) 
    fighter.shape(fighterturn[fighterturningangle])
    frtd = frtd+1
    
def fighter_forward():
    fighter.forward(1.5*FORWARD_SPEED)

def fighter_shoot():
    return

def borders_of_jet():
    jx = jet.xcor()
    jy = jet.ycor()
    
    if (jx>RIGHT_EDGE):
        jet.setx(-1*jx+5)
        
    if (jx<LEFT_EDGE):
        jet.setx(-1*jx-5)
        
    if (jy>TOP_EDGE):
        jet.sety(-1*jy+5)
        
    if (jy<BOTTOM_EDGE):
        jet.sety(-1*jy-5)

def borders_of_fighter():
    fx = fighter.xcor()
    fy = fighter.ycor()
    
    if (fx>RIGHT_EDGE):
        fighter.setx(-1*fx+5)
        
    if (fx<LEFT_EDGE):
        fighter.setx(-1*fx-5)
        
    if (fy>TOP_EDGE):
        fighter.sety(-1*fy+5)
        
    if (fy<BOTTOM_EDGE):
        fighter.sety(-1*fy-5)

def score_board():
    global p1,p2
    jet_prompt = "jet: " + str(p1)
    fighter_prompt = "fighter: " + str(p2)
    score_prompt = jet_prompt + " " + fighter_prompt
    score.write (score_prompt, align="center", font=("Roboto", 20, "bold"))

def pause():
   global paused
   if (paused == True):
      paused = False
   elif (paused == False):
      paused = True
def Quit():
    paused = True
    q = screen.textinput("Quit", "Are you sure you want to quit?(yes or no)")
    if q == "yes":
        turtle.bye()
    else:
        paused = False

def ataj_activator():
    global ataj_active
    ataj_active = True

def ata_jet_follow():
    global ataj_active
    if (ataj_active==False):
        ata_jet.pu()
        ata_jet.goto(jet.xcor(),jet.ycor())
        ata_jet.setheading(jet.heading())

def ata_jet_seek():
    global ataj_active
    if ataj_active:
        ata_jet.pd()
        ataj_xdist = ata_jet.xcor()-fighter.xcor()+.0000000000000000001
        ataj_ydist = ata_jet.ycor()-fighter.ycor()+.0000000000000000001
        ataj_rel_ang = math.degrees(tan(ataj_ydist/ataj_xdist))
        if (ata_jet.xcor()>fighter.xcor() and ata_jet.ycor()>fighter.ycor()):
            ataj_rel_ang-=180
        if (ata_jet.xcor()>fighter.xcor() and ata_jet.ycor()<fighter.ycor()):
            ataj_rel_ang-=90
        ata_jet.setheading(ataj_rel_ang)
        ata_jet.forward(FORWARD_SPEED*1.7)
        if abs(ata_jet.xcor() - fighter.xcor())<10 and abs(ata_jet.ycor() - fighter.ycor()) <10:
             ataj_active = False   
             ata_jet.clear()
 
def ataf_activator():
    global ataf_active
    ataf_active = True

def ata_fighter_follow():
    global ataf_active
    if (ataf_active==False):
        ata_fighter.pu()
        ata_fighter.goto(fighter.xcor(),fighter.ycor())
        ata_fighter.setheading(fighter.heading())
        
def ata_fighter_seek():
    global ataf_active
    if ataf_active:
        ata_fighter.pd()
        ataf_xdist = ata_fighter.xcor()-jet.xcor()+.0000000000000000001
        ataf_ydist = ata_fighter.ycor()-jet.ycor()+.0000000000000000001
        ataf_rel_ang = math.degrees(tan(ataf_ydist/ataf_xdist))
        if (ata_fighter.xcor()>jet.xcor() and ata_fighter.ycor()>jet.ycor()):
            ataf_rel_ang-=180
        if (ata_fighter.xcor()>jet.xcor() and ata_fighter.ycor()<jet.ycor()):
            ataf_rel_ang-=90
        ata_fighter.setheading(ataf_rel_ang)
        ata_fighter.forward(FORWARD_SPEED*1.7)
        if abs(ata_fighter.xcor() - jet.xcor())<10 and abs(ata_fighter.ycor() - jet.ycor()) <10:
             ataf_active = False   
             ata_fighter.clear()
# Constants
RIGHT_EDGE= 400
LEFT_EDGE = -400
BOTTOM_EDGE = -400
TOP_EDGE = 400
HEADING_STEP = 30
FORWARD_SPEED = 6


# Global Variables
jetturningangle = 0
jltd = 0
jrtd = 0
p1 = 0
p2 = 0
ataj_active = False
ataf_active = False

fighterturningangle = 0
fltd = 0
frtd = 0

#scoreboard
score=turtle.Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.goto (0,260)

#lists
jetturn = ["Jet30.gif", "Jet60.gif", "Jet90.gif", "Jet120.gif", "Jet150.gif", "Jet180.gif", "Jet210.gif", "Jet240.gif", "Jet270.gif", "Jet300.gif", "Jet330.gif", "Jet0.gif"]
fighterturn = ["Fighter330.gif", "Fighter300.gif", "Fighter270.gif", "Fighter240.gif", "Fighter210.gif","Fighter180.gif","Fighter150.gif", "Fighter120.gif", "Fighter90.gif", "Fighter60.gif", "Fighter30.gif","Fighter0.gif"]
jbullets = []
fbullets = []

# Screen
screen = Screen()
screen.setup(800,800)
screen.title("Jet Fighter")
screen.bgcolor("skyblue")
turtle.bgpic(picname="Sky.gif")
screen.tracer(0)

# Turtles
jet = Turtle()
turtle.addshape(name="Jet0.gif", shape=None) 
jet.shape("Jet0.gif") 
jet.penup()
jet.setx(100)

fighter = Turtle()
turtle.addshape(name="Fighter0.gif", shape=None)
fighter.shape("Fighter0.gif")
fighter.color('red')
fighter.penup()
fighter.setx(-100)
fighter.left(180)

ata_jet = Turtle()
ata_jet.color('red')
ata_jet.pu()
ata_jet.goto(jet.xcor(),jet.ycor())

ata_fighter = Turtle()
ata_fighter.color('black')
ata_fighter.pu()
ata_fighter.goto(fighter.xcor(),fighter.ycor())

paused = False
# Game Loop
while(True):
    screen.update()
    turtle.listen()
    if not (paused):
        movement()
      #  score_board()

# Make sure yall have all the rotations of the plane downloaded on your computer 
