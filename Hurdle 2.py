#### reeborg  world

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def lap():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
total_hurdles=6
while total_hurdles>0:
    lap()
    if at_goal():
        break
    total_hurdles=total_hurdles-1
 
        
    
##another method 

while at_goal()!=True:
    lap()
    
################################################################ to enter the reborg world use the link below
###https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json