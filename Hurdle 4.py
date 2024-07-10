def turn_right():
    turn_left()
    turn_left()
    turn_left()
def check():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
            

while not at_goal():
    if wall_in_front():
        check()
    else:
        move()

################################################################ to enter the reborg world use the link below
###https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json