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
# #for finaly_tour in range(6):
#    # tour()
   
# finaly = 0         # finaly = 6
# while finaly < 6:  # while finaly > 0:
#     tour()         # tour()
#     finaly += 1    # finaly -= 1

##hurdle 3

# def turn_right():  
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

    
# while not at_goal() :
#     if wall_in_front():
#          jump()
#     else:
#          move()
    
##hurdle 4
# def turn_right():  
#     turn_left()
#     turn_left()
#     turn_left()
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     while front_is_clear():
#         move()
#     turn_left()

    
# while not at_goal() :
#     if wall_in_front():
#          jump()
#     else:
#          move()
    
##project maze https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# while front_is_clear():
#     move()
# turn_left()
    
# while not at_goal():
#     if right_is_clear():
#           turn_right()
#           move()
#     elif front_is_clear():
#           move()
#     else:
#           turn_left()