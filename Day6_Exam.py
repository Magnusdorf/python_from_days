# def my_function():  #create a function
#     print("Hello")
#     print("Bye")

# my_function()

#link# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# def tour():    
#     move()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()
#     turn_left()
#     turn_left()
#     move()
#     turn_left()

# for finaly_tour in range(6):
#     tour()

#####################

#while loop

def tour():    
    move()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
#for finaly_tour in range(6):
   # tour()
   
finaly = 0         # finaly = 6
while finaly < 6:  # while finaly > 0:
    tour()         # tour()
    finaly += 1    # finaly -= 1
