def turn_right():
    turn_left()
    turn_left()
    turn_left()
def lap():
    
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        lap()
    else:
        move()
################################################################ to enter the reborg world use the link below
###https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json