#project

# bill = float(input("What was the total bill? "))
# people = float(input("How many people to split the bill? "))
# percentage = float(input("What percentage tip would you like to given? "))
# total_bill = float((bill + percentage) / people)
# print(f"amount to be paid per person : {total_bill} ")

#end

#String

# print("Hello"[0])

# say =  "Hello"
# print(say[3])

#Integer

# print(123 + 123)

# print(123_13_13)

#Float

# num_pi = 3.14
# print(num_pi, type(num_pi))

#Boolen  True/False

# num_char = len(input("What is your name? "))
# num_char = str(num_char) # new_num_char = str(num_char)
# print("Your anme has " + num_char + " characters.")
# print(type(num_char))

# print(55 + float("565.5"))
# print("Hi " + "Boy")


# Write a program that adds the digits in a 2 digit number. e.g. if the input was 34, then the output should be 3 + 4 = 7

# two_digit_number = input("Type a two digit number: ")

# first_digit = two_digit_number[0]
# second_digit = two_digit_number[1]

# first_digit = int(first_digit)
# second_digit = int(second_digit)
# ## result = int(first_digit) + int(second_ digit)
# ##print(result)
# print(first_digit + second_digit)

# project Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# height = float(input("enter your height in m : "))
# weight = float(input("enter your weight in kg: "))
# bmi = (weight / (height ** 2))
# print(bmi)

# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# bmi = float(weight) / (float(height) ** 2)
# print(int(bmi))

# print(round(22 / 3))
# print(round(20 / 3))  
# print((round(23 / 4, 2)))  # 5.75
# print(round(23 / 4, 1))  #5.8
# print(round(7.53324, 2))  #5.53

#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# age = input("What is your current age? ")

# remaining_age = 90 - int(age)

# z = remaining_age * 12
# y = z * 4
# x = y * 7

# print(f"You have {x} days, {y} weeks and {z} months left.")
# #                   #                           #                     #                                 #                        #
# age = input("What is your current age? ")

# remaining_age = 90 - int(age)

# z = remaining_age * 12
# y = remaining_age * 52
# x = remaining_age * 365

# print(f"You have {x} days, {y} weeks and {z} months left.")
