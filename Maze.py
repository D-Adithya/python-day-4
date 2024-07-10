def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        
    elif front_is_clear():
            move()
    else:
            turn_left()

################################################################ to enter the reborg world use the link below
###https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json