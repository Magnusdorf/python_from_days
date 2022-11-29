# import random
# random_int = random.randint(1, 10)
# print(random_int)  #random numbers


# random_float = random.random()
# print(random_float)

#You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

# import random
##way1
# money = ['Heads', 'Tails']
# random_change = random.choice(money)
# print(random_change)
##way2
# random_side = random.randint(0, 1)
# if random_side == 1:
#     print('Heads')
# else :
#     print('Tails')

# states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina',
# 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana',
# 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin',
# 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota',
# 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']

# print(states_of_america[2])
# print(states_of_america[10])  #index number
# print(states_of_america[-1])

# states_of_america.append('NewCity')  #add an item to the of the list.
# print(states_of_america[-1])

# states_of_america.extend(['Magnusland', 'Dorfland'])  # extend the list by appending all the items from the iterable.
# print(states_of_america)

#project
# You are going to write a program that will select a random name from a list of names.
#  The person selected will have to pay for everybody's food bill.
# that was wrong #

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# import random

# random_names = random.randint(0, 4)
# if random_names == 1 :
#     print(f'{random_names} is going to buy the meal today!')
# elif random_names == 2 :
#     print(f'{random_names} is going to buy the meal today!')
# elif random_names == 3 :
#     print(f'{random_names} is going to buy the meal today!')
# elif random_names == 4 :
#     print(f'{random_names} is going to buy the meal today!')
# else :
#     print(f'{random_names} is going to buy the meal today!')

#True

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# import random
# x = len(names)

# random_name = random.randint(0, x - 1)
# person_pay = names[random_name]
# print(person_pay + "is going to buy the meal today ")

# on't change the code below 


# row1 = ["⬜️","️⬜️","️⬜️"]
# row2 = ["⬜️","⬜️","️⬜️"]
# row3 = ["⬜️️","⬜️️","⬜️️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")

# position = input("Where do you want to put the treasure? ")
# horizonal = int(position[0])
# vertical = int(position[1])

# selected_row = map[vertical - 1]
# selected_row[horizonal - 1] = 'X'

# #Write your code above this row 

# # on't change the code below 
# print(f"{row1}\n{row2}\n{row3}")


# project #

# import random

# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''

# game_images = [rock, paper, scissors]
# user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])

# computer_choice = random.randint(0, 2)
# print(f"Computer chose \n{computer_choice}")
# print(game_images[computer_choice])

# if user_choice >= 3 :
#     print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2 :
#     print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#     print("You lose!")
# elif computer_choice > user_choice :
#     print("You Lose!")
# elif user_choice > computer_choice :
#     print("You win!")
# elif computer_choice == user_choice:
#     print("It's a draw")
# elif user_choice >= 3 :
#     print("You typed an invalid number, you lose!")
# else :
#     print("You typed an invalid number, you lose! ")