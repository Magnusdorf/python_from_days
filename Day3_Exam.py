# project
# Write a program that works out whether if a given number is an odd or even number.

# # Don't change the code below 
# number = int(input("Which number do you want to check? "))
# # on't change the code above 

# #Write your code below this line 

# if number%2 == 0 :
#     print("This is an even number.")
# else :
#     print("This is an odd number.")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ? "))
# if height >= 120:
#     print("You can ride the rollercoaster.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ? "))


# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("What is your age? "))
#     if age < 12 :
#         print("Please pay $5")
#     elif age <= 18:
#         print("Please pay $7")
#     else:
#         print("Please pay $12")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# # Don't change the code below 👇
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
# # Don't change the code above 👆

# #Write your code below this line 👇

# BMI = weight/(height ** 2)
# BMI = round(BMI, 1)

# if BMI < 18.5 :
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25 :
#     print(f"Your BMI is {BMI}, you have a normal weight.")
# elif BMI < 30 :
#     print(f"Your BMI is {BMI}, you are slightly overweight.")
# elif BMI < 35 :
#     print(f"Your BMI is {BMI}, you are obese.")
# else :
#     print(f"Your BMI is {BMI} , you are clinically obese..")

# Write a program that works out whether if a given year is a leap year.

# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.") 
#         else:
#             print("Not Leap year.")
#     else: 
#         print("Leap year.")
# else: 
#     print("Not leap year.")

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm ? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("What is your age? "))
#     if age < 12 :
#         bill = 5
#         print("Chield tickets are $5")
#     elif age <= 18:
#         bill = 7
#         print("Youth tickets are $7")
#     else:
#         bill = 12
#         print("Adult tickets are $12")
#     photo = input("Wants photos ? Y/N ")
#     if photo == "Y" :
#         bill += 3
#         print(f"Your final bill is ${bill}")
#     elif photo == "N":
#         print(f"Your final bill is ${bill}")
#     else:
#         print("Please Enter : Y or N")
        
# else:
#     print("Sorry, you have to grow taller before you can ride.")

#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L :")
# add_pepperoni = input("Do you want pepperoni? Y or N :")
# extra_cheese = input("Do you want extra cheese? Y or N :")
# bill = 0
# if size == "S" :
#     bill += 15
#     if add_pepperoni == "Y" :
#         bill +=2
#     elif add_pepperoni == "N":
        
#         if extra_cheese == "Y":
#             bill += 1
#         elif extra_cheese == "N":
#             print(f"Your final bill is: ${bill}")
#     print(f"Your final bill is: ${bill}")
# if size == "M" :
#     bill += 20
#     if add_pepperoni == "Y" :
#         bill +=3
#     elif add_pepperoni == "N":
#         print(f"Your final bill is: ${bill}")
#         if extra_cheese == "Y":
#             bill += 1
#         elif extra_cheese == "N":
#             print(f"Your final bill is: ${bill}")
#     print(f"Your final bill is: ${bill}")
# if size == "L" :
#     bill += 25
#     if add_pepperoni == "Y" :
#         bill +=3
#     elif add_pepperoni == "N":
#         if extra_cheese == "Y":
#             bill += 1
#         elif extra_cheese == "N":
#               print(f"Your final bill is: ${bill}")



print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L :")
add_pepperoni = input("Do you want pepperoni? Y or N :")
extra_cheese = input("Do you want extra cheese? Y or N :")
bill = 0

if size == "S":
    bill +=15
elif size == "M" :
    bill +=20
else:
    bill+=25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else :
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")


