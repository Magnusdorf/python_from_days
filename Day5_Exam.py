# fruits = ['Apple', 'Peach', 'Pear']

# for fruit in fruits:
#     print(fruit)
#     print(fruit + ' Pie')

# You are going to write a program that calculates the average student height from a List of heights.

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# total_heights = 0
# for height in student_heights:
#     total_heights += height
# # print(total_heights)

# number_of_students = 0
# for students in student_heights:
#     number_of_students += 1
# # print(number_of_students)

# average_height = round(total_heights / number_of_students)
# print(average_height)



# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is : {highest_score}")

# #for loop with range 
# for number in range(1, 10):
#     print(number)

# for num in range(1, 22, 4):
#     print(num)

# total = 0 
# for num in range(1, 101):
#     total += num
# print(total)

# total_num = 0
# for x in range(2, 101, 2):
#     total_num += x
# print(total_num)

# for num in range(1, 101):
#     if num % 15 == 0:
#         print("FizzBuzz")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     else:
#         print(num)


# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0 :
#         print("FizzBuzz")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     else:
#         print(num)

#project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")