# Jet Fighter
import turtle
from turtle import *
import math
from math import tan
import re
import random
from threading import Timer

# Functions
#all of the movement functions for the jet and fighter take the global variable paused

#this function uses the turtle.listen() function and tells the
#game what to do when a button is pressed. It also moves the planes forward,
#calls all the functions that handle flares, air-to-air missiles, pausing, and quitting
#also handles borders of the planes
def movement():
    global pp1,pp2
    pp1 = p1; pp2 = p2
    jet.forward(FORWARD_SPEED)
    fighter.forward(FORWARD_SPEED)
    ata_jet_follow()
    aj = ata_jet_seek()
    ata_jet_borders(aj)
    ata_fighter_follow()
    af = ata_fighter_seek()
    ata_fighter_borders(af)

    turtle.onkey(jet_left,"Left")
    turtle.onkey(jet_right,"Right")
    turtle.onkey(jet_forward,"Up")
    turtle.onkey(jet_shoot,"Down")
    jet_bullet_moving()
    turtle.onkey(ataj_activator,"/")
    turtle.onkey(j_flares,".")
    
    turtle.onkey(fighter_left,"a")
    turtle.onkey(fighter_right,"d")
    turtle.onkey(fighter_forward,"w")
    turtle.onkey(fighter_shoot,"s")
    fighter_bullet_moving()
    turtle.onkey(ataf_activator,"e")
    turtle.onkey(f_flares,"f")
    
    turtle.onkey(pause, "space")
    turtle.onkey(Quit, "Q")
    
    j_flares_movement()
    f_flares_movement()
    
    borders_of_jet()
    borders_of_fighter()

    

#this function occurs when the left arrow key is pressed.
#it takes no parameters but uses three global variables, jet turning
#angle, jltd, and jrtd. It subtracts frum the jet turning angle
def jet_left():
    global jetturningangle, jltd, jrtd, paused
    if not paused:
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
    else:
        return


#This functions occurs when the right arrow key is pressed. It has
#no parameters but uses the global variables jet turning angle, jrtd, and jltd
#It adds to jet turning angle and turns the plane right 30 degrees
def jet_right():
    global jetturningangle, jrtd, jltd, paused
    if not paused:
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
    else:
        return

#this function serves as a kind of boost when the up arrow key is pressed.
#it moves the jet forward 1.5 times the forward speed
def jet_forward():
    global paused
    if not paused:
        jet.forward(1.5*FORWARD_SPEED)
    else:
        return
    
#this function is called when 's' is pressed
#this function spawns in bullets for the jet if there are no bullets spawned
#if there are bullets, they are teleported to the plane and set to the same heading as the plane
def jet_shoot():
    global paused
    if not paused:
        if len(jbullets)<5:
            jbullets.append([Turtle(),False])
            last_turtle = jbullets[len(jbullets)-1][0]
            last_turtle.setheading(jet.heading())
            last_turtle.pu()
            last_turtle.shape('circle')
            last_turtle.color('red')
            last_turtle.shapesize(.1,.1,.1)
            last_turtle.goto(jet.xcor(),jet.ycor())
        elif len(jbullets)>=5:
            first_elem = jbullets[0]
            first_turtle = first_elem[0]
            out_o_b = first_elem[1]
            if (out_o_b):
                first_turtle.goto(jet.xcor(),jet.ycor())
                first_turtle.setheading(jet.heading())
                jbullets.remove(first_elem)
                jbullets.append([first_elem[0],False])
        else:
            return

#this function handles bullet movement for the jet and checks whether bullets are in bounds
#if bullets are out of bounds, and what happens upon collision with the fighter
#then they are kept at a coordinate off screen until shot again
def jet_bullet_moving():
    for turt in jbullets:
        turt[0].pu()
        out_of_bounds = False
        if not turtle_inbound(turt[0]):
            turt[0].goto(650,0)
            mover = 0
            out_of_bounds = True
        elif red_bullet_collision(turt):
            turt[0].goto(650,0)
            mover = 0
            out_of_bounds = True
        else:
            mover = BULLET_SPEED_MULTIPLIER
        if out_of_bounds or (turt[1]==True):
            turt.remove(turt[1])
            turt.append(True)
        else:
            turt.remove(turt[1])
            turt.append(False)
        turt[0].forward(FORWARD_SPEED*mover)

#this function changes the image and heading of the fighter 30 degrees right. It takes
#3 global variables. 
def fighter_right():
    global fighterturningangle, frtd, fltd, paused
    if not paused:
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
    else:
        return

#this function changes the image and heading of the fighter 30 degrees left. It takes
#3 global variable
def fighter_left():
    global fighterturningangle, fltd, frtd, paused
    if not paused:
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
    else:
        return

#this fighter serves as a boost for the fighter. It takes no variables.
def fighter_forward():
    global paused
    if not paused:
        fighter.forward(1.5*FORWARD_SPEED)
    else:
        return
    
#this function is called when 's' is pressed
#this function spawns in bullets for the fighter if there are no bullets spawned
#if there are bullets, they are teleported to the plane and set to the same heading as the plane
def fighter_shoot():
    global paused
    if not paused:
        if len(fbullets)<5:
            fbullets.append([Turtle(),False])
            last_turtle = fbullets[len(fbullets)-1][0]
            last_turtle.setheading(fighter.heading())
            last_turtle.pu()
            last_turtle.shape('circle')
            last_turtle.shapesize(.1,.1,.1)
            last_turtle.goto(fighter.xcor(),fighter.ycor())
        elif len(fbullets)>=5:
            first_elem = fbullets[0]
            first_turtle = first_elem[0]
            out_o_b = first_elem[1]
            if (out_o_b):
                first_turtle.goto(fighter.xcor(),fighter.ycor())
                first_turtle.setheading(fighter.heading())
                fbullets.remove(first_elem)
                fbullets.append([first_elem[0],False])
    else:
        return
            
#this function handles bullet movement for the fighter and checks whether bullets are in bounds
#if bullets are out of bounds, and what happens upon collision with the jet
#then they are kept at a coordinate off screen until shot again
def fighter_bullet_moving():
    for turt in fbullets:
        turt[0].pu()
        out_of_bounds = False
        if not turtle_inbound(turt[0]):
            turt[0].goto(650,0)
            mover = 0
            out_of_bounds = True
        elif black_bullet_collision(turt):
            turt[0].goto(650,0)
            mover = 0
            out_of_bounds = True
        else:
            mover = BULLET_SPEED_MULTIPLIER
        if out_of_bounds or (turt[1]==True):
            turt.remove(turt[1])
            turt.append(True)
        else:
            turt.remove(turt[1])
            turt.append(False)
        turt[0].forward(FORWARD_SPEED*mover)

#this function detects a collision between any edge and the jet, and sends the jet
#to the opposite side
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

#this function detects a collision between any edge and the fighter, and sends the
#fighter to the opposite side
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
        
#this handles the scoreboard outside of the main loop to prevent lag
def first_time_scoreboard():
    score.clear()
    jet_prompt = p_names[0]
    fighter_prompt = p_names[1]
    score_prompt = fighter_prompt + ": " +str(p2) + "      " + jet_prompt + ": " + str(p1)
    score.write (score_prompt, align="center", font=("Roboto", 30, "bold"))
    jet_HUD()
    fighter_HUD()

#this puts the health of both players on the top of the screen. It accepts pp1 and pp2,
#as well as the globals p1 and p2. It also calls the winning function
def health_display(pp1,pp2):
    global p1, p2
    if pp1!=p1 or pp2!=p2:
        score.clear()
        jet_prompt = p_names[0]
        fighter_prompt = p_names[1]
        score_prompt = fighter_prompt + ": " +str(p2) + "      " + jet_prompt + ": " + str(p1)
        score.write (score_prompt, align="center", font=("Roboto", 30, "bold"))
        winning()

#this function is called in health_display and takes the globals p1, p2, and paused.
#it checks if either of the players have no health left and changes their planes into
#explosions.    
def winning():
    global p1, p2, paused
    fx = fighter.xcor()
    fy = fighter.ycor()
    jx = jet.xcor()
    jy = jet.ycor()

    if p1 <= 0:
        jet.shape('explosion.gif')
        ata_jet.shape('explosion.gif')
        ata_fighter.clear()
        paused = True
        score.clear()
        score.color("red")
        
        if jy > 0:
            score.goto(0,-250)
            score.write(p_names[1]+" Wins!", align="center", font=("Courier", 75, "bold"))
        if jy <= 0:
            score.goto(0,200)
            score.write(p_names[1]+" Wins!", align="center", font=("Courier", 75, "bold"))

    if p2 <= 0:
        fighter.shape('explosion.gif')
        ata_fighter.shape('explosion.gif')
        ata_jet.clear()
        paused = True
        score.clear()
        
        if fy > 0:
            score.goto(0,-250)
            score.write(p_names[0]+" Wins!", align="center", font=("Courier", 75, "bold"))
        if fy <= 0:
            score.goto(0,200)
            score.write(p_names[0]+" Wins!", align="center", font=("Courier", 75, "bold"))

#this function is called when the space bar is pressed. It changes the paused global
#variable depending on the condition
def pause():
   global paused
   if (paused == True):
      paused = False
   elif (paused == False):
      paused = True

#this function occers when shift+q is pressed. It asks the users if they want to quit
def Quit():
    paused = True
    q = screen.textinput("Quit", "Are you sure you want to quit?(yes or no)")
    if re.match("^[y, Y]", q):
        turtle.bye()
    else:
        paused = False

        
#this is the activator for the jet's ata missile. It occurs when "/" is hit.
#it takes the globals ataj_active, jet_ata_cooldown, jcooldown_happened, and
#jtimer_active
#it uses the threading import to create a timer for the cooldown function.
def ataj_activator():
    global ataj_active, jet_ata_cooldown, jcooldown_happened, jtimer_active, paused
    if not paused:
        if jtimer_active == False:
            if jet_ata_cooldown == True:
                ata_jet.hideturtle()
                jt = Timer(7, ataj_cooldown)
                jt.start()
                ataj_active = False
                jtimer_active = True

            if jet_ata_cooldown == False:
                ataj_active = True

            if jcooldown_happened == True:
                Timer(7, ataj_cooldown).cancel()
                jcooldown_happened = False
                jet_ata_cooldown = False
                jtimer_active = False
        else:
            return
    else:
        return

#this function is called by the timer and uses the variables jcooldown_happened,
#jtimer_active, and jet_ata_cooldown.
#it changes the variables for conditionals in other functions and makes the ata visible
def ataj_cooldown():
    global jcooldown_happened, jtimer_active, jet_ata_cooldown
    ata_jet.showturtle()
    jcooldown_happened = True
    jtimer_active = False
    jet_ata_cooldown = False

#When the jet's air-to-air (ata) missile is inactive, it stays onboard the plane
#this function keeps the ata on the jet until launched
def ata_jet_follow():
    global ataj_active
    if (ataj_active==False):
        ata_jet.pu()
        ata_jet.goto(jet.xcor(),jet.ycor())
        ata_jet.setheading(jet.heading())
        

# to find the angle of which the ata should go, trigonometry is used. 
# using the x and y distance, and tangent, we can get the desired angle. 
# the consecutive set of if statments is to make sure the ata is on the right course
# jet_ata_lock() is a function that makes sure flares are a possible target for the ata
# if a collision is detected, health is reduced accordingly
def ata_jet_seek():
    global ataj_active, p1, jet_ata_cooldown
    if ataj_active:
        ata_jet.pd()
        j_ata_target = jet_ata_lock()
        ataj_xdist = ata_jet.xcor()-j_ata_target.xcor()+.0000000000000000001
        ataj_ydist = ata_jet.ycor()-j_ata_target.ycor()+.0000000000000000001
        ataj_rel_ang = math.degrees(tan(ataj_ydist/ataj_xdist))
        if (ata_jet.xcor()>j_ata_target.xcor() and ata_jet.ycor()>j_ata_target.ycor()):
            ataj_rel_ang-=180
        if (ata_jet.xcor()>j_ata_target.xcor() and ata_jet.ycor()<j_ata_target.ycor()):
            ataj_rel_ang-=90
        ata_jet.setheading(ataj_rel_ang)
        ata_jet.forward(FORWARD_SPEED*ATA_SPEED_MULTIPLIER)
        if abs(ata_jet.xcor() - fighter.xcor())<10 and abs(ata_jet.ycor() - fighter.ycor()) <10:
             ataj_active = False   
             ata_jet.clear()
             global p2
             p2-=15
             ata_jet_follow()
             jet_ata_cooldown = True
             ataj_activator()
        return (ataj_rel_ang)

#this function is to prevent the ata from going far off of the screen. It takes aj,
#which is ataj_rel_angle, and adds 180 degrees to it so it bounces off of the wall.
def ata_jet_borders(aj):
    global ataj_active
    ax = ata_jet.xcor()
    ay = ata_jet.ycor()
    if ataj_active:
        ataj_rel_angle = int(aj)
        turn_angle = ataj_rel_angle + 180
        if (ax>RIGHT_EDGE): 
            ata_jet.setheading(turn_angle)
            ata_jet.forward(30)
            
        if (ax<LEFT_EDGE):    
            ata_jet.setheading(turn_angle)
            ata_jet.forward(30)
            
        if (ay>TOP_EDGE): 
            ata_jet.setheading(turn_angle)
            ata_jet.forward(30)
          
        if (ay<BOTTOM_EDGE): 
            ata_jet.setheading(turn_angle)
            ata_jet.forward(30)

#this is the activator for the fighter's ata missile. It occurs when "e" is hit.
#it takes the globals ataf_active, fighter_ata_cooldown, fcooldown_happened, and
#ftimer_active
#it uses the threading import to create a timer for the cooldown function.
def ataf_activator():
    global ataf_active, fighter_ata_cooldown, fcooldown_happened, ftimer_active, paused
    if not paused:
        if ftimer_active == False:
            if fighter_ata_cooldown == True:
                ata_fighter.hideturtle()
                ft = Timer(7, ataf_cooldown)
                ft.start()
                ataf_active = False
                ftimer_active = True

            if fighter_ata_cooldown == False:
                ataf_active = True

            if fcooldown_happened == True:
                Timer(7, ataf_cooldown).cancel()
                fcooldown_happened = False
                fighter_ata_cooldown = False
                ftimer_active = False
        else:
            return
    else:
        return

#this function is called by the timer and uses the variables fcooldown_happened,
#ftimer_active, and fighter_ata_cooldown.
#it changes the variables for conditionals in other functions and makes the ata visible
def ataf_cooldown():
    global fcooldown_happened, ftimer_active, fighter_ata_cooldown
    ata_fighter.showturtle()
    fcooldown_happened = True
    ftimer_active = False
    fighter_ata_cooldown = False

#When the fighter's air-to-air (ata) missile is inactive, it stays onboard the plane
#this function keeps the ata on the jet until launched
def ata_fighter_follow():
    global ataf_active
    if (ataf_active==False):
        ata_fighter.pu()
        ata_fighter.goto(fighter.xcor(),fighter.ycor())
        ata_fighter.setheading(fighter.heading())
        
# to find the angle of which the ata should go, trigonometry is used. 
# using the x and y distance, and tangent, we can get the desired angle. 
# the consecutive set of if statments is to make sure the ata is on the right course
# fighter_ata_lock() is a function that makes sure flares are a possible target for the ata
# if a collision is detected, health is reduced accordingly
def ata_fighter_seek():
    global ataf_active, p2, fighter_ata_cooldown
    if ataf_active:
        ata_fighter.pd()
        f_ata_target = fighter_ata_lock()
        ataf_xdist = ata_fighter.xcor()-f_ata_target.xcor()+.0000000000000000001
        ataf_ydist = ata_fighter.ycor()-f_ata_target.ycor()+.0000000000000000001
        ataf_rel_ang = math.degrees(tan(ataf_ydist/ataf_xdist))
        if (ata_fighter.xcor()>f_ata_target.xcor() and ata_fighter.ycor()>f_ata_target.ycor()):
            ataf_rel_ang-=180
        if (ata_fighter.xcor()>f_ata_target.xcor() and ata_fighter.ycor()<f_ata_target.ycor()):
            ataf_rel_ang-=90
        ata_fighter.setheading(ataf_rel_ang)
        ata_fighter.forward(FORWARD_SPEED*ATA_SPEED_MULTIPLIER)
        if abs(ata_fighter.xcor() - jet.xcor())<10 and abs(ata_fighter.ycor() - jet.ycor()) <10:
             ataf_active = False   
             ata_fighter.clear()
             global p1
             p1-=15
             ata_fighter_follow()
             fighter_ata_cooldown = True
             ataf_activator()
        return (ataf_rel_ang)

#this function is to prevent the ata from going far off of the screen. It takes af,
#which is ataf_rel_angle, and adds 180 degrees to it so it bounces off of the wall.
def ata_fighter_borders(af):
    global ataf_active
    ax = ata_fighter.xcor()
    ay = ata_fighter.ycor()
    if ataf_active:
        ataf_rel_angle = int(af)
        turn_angle = ataf_rel_angle + 180
        if (ax>RIGHT_EDGE): 
            ata_fighter.setheading(turn_angle)
            ata_fighter.forward(30)
            
        if (ax<LEFT_EDGE):    
            ata_fighter.setheading(turn_angle)
            ata_fighter.forward(30)
            
        if (ay>TOP_EDGE): 
            ata_fighter.setheading(turn_angle)
            ata_fighter.forward(30)
          
        if (ay<BOTTOM_EDGE): 
            ata_fighter.setheading(turn_angle)
            ata_fighter.forward(30)
            
# checks for whether the bullets shot from the jet hit the fighter, and reduces the health accordingly
def red_bullet_collision(turt):
    if abs(turt[0].xcor() - fighter.xcor())<20 and abs(turt[0].ycor() - fighter.ycor()) <20:
        collision = True
        global p2
        p2-=5
    else:
        collision = False
    return collision

# checks for whether the bullets shot from the fighter hit the jet, and reduces the health accordingly
def black_bullet_collision(turt):
    if abs(turt[0].xcor() - jet.xcor())<20 and abs(turt[0].ycor() - jet.ycor()) <20:
        collision = True
        global p1
        p1-=5
    else:
        collision = False
    return collision

# if there are still inactive flares to use, this function sets the position of and heading of the flares
# the used flares are then appended to the list of the jet's active flares and removed from the inactive list
# flares are launched in groups of two
def j_flares():
    global paused
    if not paused:
        if (len(inactive_jet_flares) > 0):
            launch_heading = 100
            for turt in inactive_jet_flares[0]:
                turt.showturtle()
                turt.goto(jet.xcor(),jet.ycor())
                turt.setheading(jet.heading()-launch_heading)
                launch_heading*=-1
            j_active_flares.append(inactive_jet_flares[0])
            inactive_jet_flares.remove(inactive_jet_flares[0])
            jet_HUD()
    else:
        return

# this function formats all the flares for the fighter as white circles
def jet_flares_formatting():
    for turt_group in inactive_jet_flares:
        for turt in turt_group:
            turt.pu()
            turt.shape('circle')
            turt.color('white')
            turt.shapesize(.2,.2,.2)
            turt.goto(650,10)

# for every flare group in the active flare list, the speed of the flares if checked if its under .65
# if the speed is slower than .65, the flares are taken off screen, and made immobile
# if the speed is higher than .65, then the speed is used the in forward() function, and then reduced by .99
def j_flares_movement():
    global j_flare_active
    if len(j_active_flares) > 0:
        for turt_group in j_active_flares:
            group_loc = j_active_flares.index(turt_group)
            breaker = False
            if (jet_flares_speed[group_loc] < 0.65): 
                turt_group[0].goto(650,20)
                turt_group[1].goto(650,20)
                breaker = True
                jet_flares_speed[group_loc] = 0
            for turt in turt_group:
                if (breaker):
                    break
                turt.forward(.3*jet_flares_speed[group_loc])
                jet_flares_speed[group_loc]*=.99

# this function chooses which target the fighter's ata missiles lock onto 
# all of the jet's active flares and the jet are added to a list of targets, 
# and a target is randomly chosen from the list, causing the ata to go crazy
def fighter_ata_lock():
    for flare_group in j_active_flares:
        for flare_inb in flare_group:
            if turtle_inbound(flare_inb):
                fighter_ata_targets.append(flare_inb)
    fighter_ata_targets.append(jet)
    f_ata_target = random.choice(fighter_ata_targets)
    fighter_ata_targets.clear()
    return f_ata_target

# if there are still inactive flares to use, this function sets the position of and heading of the flares
# the used flares are then appended to the list of the fighter's active flares and removed from the inactive list
# flares are launched in groups of two
def f_flares():
    global paused
    if not paused:
        if len(inactive_fighter_flares) > 0:
            launch_heading = 100
            for turt in inactive_fighter_flares[0]:
                turt.showturtle()
                turt.goto(fighter.xcor(),fighter.ycor())
                turt.setheading(fighter.heading()-launch_heading)
                launch_heading*=-1
            f_active_flares.append(inactive_fighter_flares[0])
            inactive_fighter_flares.remove(inactive_fighter_flares[0])
            fighter_HUD()
    else:
        return
    
# this function formats all the flares for the fighter as white circles
def fighter_flares_formatting():
    for turt_group in inactive_fighter_flares:
        for turt in turt_group:
            turt.pu()
            turt.shape('circle')
            turt.color('white')
            turt.shapesize(.2,.2,.2)
            turt.goto(650,-10)

# for every flare group in the active flare list, the speed of the flares if checked if its under .65
# if the speed is slower than .65, the flares are taken off screen, and made immobile
# if the speed is higher than .65, then the speed is used the in forward() function, and then reduced by .99
def f_flares_movement():
    if len(f_active_flares)>0:
        for turt_group in f_active_flares:
            group_loc = f_active_flares.index(turt_group)
            breaker = False
            if (fighter_flares_speed[group_loc] < 0.65): 
                turt_group[0].goto(650,20)
                turt_group[1].goto(650,20)
                breaker = True
                fighter_flares_speed[group_loc] = 0
            for turt in turt_group:
                if (breaker):
                    break
                turt.forward(.3*fighter_flares_speed[group_loc])
                fighter_flares_speed[group_loc]*=.99

# this function chooses which target the jet's ata missiles lock onto 
# all of the fighter's active flares and the fighter are added to a list of targets, 
# and a target is randomly chosen from the list, causing the ata to go crazy
def jet_ata_lock():
    for flare_group in f_active_flares:
        for flare_inb in flare_group:
            if turtle_inbound(flare_inb):
                jet_ata_targets.append(flare_inb)
    jet_ata_targets.append(fighter)
    j_ata_target = random.choice(jet_ata_targets)
    jet_ata_targets.clear()
    return j_ata_target

# this function tests whether the passed in turtle is in-bounds
# it returns either true or false
def turtle_inbound(turtl):
    x_inb = True
    y_inb = True
    if turtl.xcor()>RIGHT_EDGE or turtl.xcor()<LEFT_EDGE:
        x_inb = False
    if turtl.ycor()>TOP_EDGE or turtl.ycor()<BOTTOM_EDGE:
        y_inb = False
    if x_inb==False or y_inb==False:
        return False
    elif x_inb==True or y_inb==True:
        return True
        
# prints the number of flares left for the jet on-screen
def jet_HUD():
    j_hud_pen.clear()
    flare_info = 'flares: ' + str(len(inactive_jet_flares))
    j_hud_pen.write(flare_info, align="center", font=("Roboto", 17, "bold"))
    
# prints the number of flares left for the fighter on-screen
def fighter_HUD():
    f_hud_pen.clear()
    flare_info = 'flares: ' + str(len(inactive_fighter_flares))
    f_hud_pen.write(flare_info, align="center", font=("Roboto", 17, "bold"))

#this function asks the players for their usernames and puts them into a list
def choose_names():
    p1_name = screen.textinput("Player 1", "What is Player 1's name?(black jet)")
    p_names.append(p1_name)
    p2_name = screen.textinput("Player 2", "What is Player 2's name?(red jet)")
    p_names.append(p2_name)

# Constants
RIGHT_EDGE= 400
LEFT_EDGE = -400
BOTTOM_EDGE = -400
TOP_EDGE = 400
HEADING_STEP = 30
FORWARD_SPEED = 6
MAX_FLARE_NUM = 15
ATA_SPEED_MULTIPLIER = 3
BULLET_SPEED_MULTIPLIER = 3

# Global Variables
jetturningangle = 0
jltd = 0
jrtd = 0
ataj_active = False

p1 = 100
p2 = 100

fighterturningangle = 0
fltd = 0
frtd = 0
ataf_active = False

jet_ata_cooldown = False
fighter_ata_cooldown = False

fcooldown_happened = False
jcooldown_happened = False

ftimer_active = False
jtimer_active = False

paused = False

#scoreboard
score=turtle.Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.goto (0,300)

jet_cooldown = Turtle()
jet_cooldown.speed(0)
jet_cooldown.pu()
jet_cooldown.hideturtle()
jet_cooldown.goto(-300, 305)
jet_cooldown.color("black")

fighter_cooldown = Turtle()
fighter_cooldown.speed(0)
fighter_cooldown.pu()
fighter_cooldown.hideturtle()
fighter_cooldown.color("red")
fighter_cooldown.goto(300, 305)

#lists
jetturn = ["Jet30.gif", "Jet60.gif", "Jet90.gif", "Jet120.gif", "Jet150.gif", "Jet180.gif", "Jet210.gif", "Jet240.gif", "Jet270.gif", "Jet300.gif", "Jet330.gif", "Jet0.gif"]
fighterturn = ["Fighter330.gif", "Fighter300.gif", "Fighter270.gif", "Fighter240.gif", "Fighter210.gif","Fighter180.gif","Fighter150.gif", "Fighter120.gif", "Fighter90.gif", "Fighter60.gif", "Fighter30.gif","Fighter0.gif"]
jbullets = []
fbullets = []

inactive_jet_flares = [[Turtle(),Turtle()] for x in range(0,MAX_FLARE_NUM)]
j_active_flares = []
jet_flares_speed = [5 for x in range(0,MAX_FLARE_NUM)]
jet_ata_targets = []

inactive_fighter_flares = [[Turtle(),Turtle()] for x in range(0,MAX_FLARE_NUM)]
f_active_flares = []
fighter_flares_speed = [5 for x in range(0,MAX_FLARE_NUM)]
fighter_ata_targets = []

p_names = []

#Create the Screen and explosion shape
screen = Screen()
screen.setup(800,800)
screen.title("Jet Fighter")
screen.bgcolor("skyblue")
turtle.bgpic(picname="Sky.gif")
screen.tracer(0)
turtle.addshape(name="explosion.gif", shape=None)

#Create the Turtles
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

jet_flares_formatting()
fighter_flares_formatting()

j_hud_pen = Turtle()
j_hud_pen.color('black')
j_hud_pen.shape('circle')
j_hud_pen.shapesize(.05,.05,.05)
j_hud_pen.pu()
j_hud_pen.goto(350,-375)
f_hud_pen = Turtle()
f_hud_pen.color('red')
f_hud_pen.shape('circle')
f_hud_pen.shapesize(.05,.05,.05)
f_hud_pen.pu()
f_hud_pen.goto(-350,-375)

#call choosing names and the first time scoreboard
choose_names()
first_time_scoreboard()

# Game Loop
while(True):
    screen.update()
    turtle.listen()
    if not (paused):
        movement()
        health_display(pp1,pp2)

# Make sure yall have all the rotations of the plane downloaded on your computer
