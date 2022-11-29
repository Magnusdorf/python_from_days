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
