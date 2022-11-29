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



# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L :")
# add_pepperoni = input("Do you want pepperoni? Y or N :")
# extra_cheese = input("Do you want extra cheese? Y or N :")
# bill = 0

# if size == "S":
#     bill +=15
# elif size == "M" :
#     bill +=20
# else:
#     bill+=25

# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else :
#         bill += 3
# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}")


# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined = name1 + name2
# lower_combined = combined.lower()

# t = lower_combined.count("t")
# r = lower_combined.count("r")
# u = lower_combined.count("u")
# e = lower_combined.count("e")

# true = t + r + u + e

# l = lower_combined.count("l")
# o = lower_combined.count("o")
# v = lower_combined.count("v")
# e = lower_combined.count("e")
# love = l + o + v + e

# love_score = int(str(true) + str(love))


# if love_score < 10 or love_score > 90 :
#     print(f"Your love score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 and love_score <= 50 :
#     print(f"Your score is {love_score}, you are alright together. ")
# else:
#     print(f"Your score is {love_score}")

print('You fell on an island and then you were given a task')
print()
print("Your mission is to find the treasure!!!")
input("Press any key to enter the island")
print()
print('Welcome to Magnus Island.')

way = input("There are two different colored roads, which one would you like to go? (Blue or Red) :")

if way == "Blue" :
    print("you saw two doors")
    door = int(input("Which door will you go through? (1 or 2) :"))
    if door == 1 :
        print("You found a motorcycle and a car")
        vehicle = input("Choose a vehicle : (car or motorcycle) :")
        if vehicle  == "car" :
            print("""  There was a bomb on the sofa :/

             *   **           * *                 
              .--------.*
              ____/_____|___ \___
             O    _   - |   _   ,*
              '--(_)-------(_)--' """)
        elif vehicle == "motorcycle" :
            print("""You drove.. you have reached the exit of the island and...
        
              r==
        _  //
       |_)//(''''':
         //  \_____:_____.-----.P
        //   | ===  |   /        \
    .:'//.   \ \=|   \ /  .:'':.
   :' // ':   \ \ ''..'--:'-.. ':
   '. '' .'    \:.....:--'.-'' .'
    ':..:'                ':..:'
""")
            ship = input("""Which ship would you like to go with? (WWS or HJW) :
        WWS :
                                        # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                                                             /
      \_______________________________________________WWS_________/


        HJW :
             __    __    __
                             |==|  |==|  |==|
                           __|__|__|__|__|__|_
                        __|___________________|___
                     __|__[]__[]__[]__[]__[]__[]__|___
                    |............................o.../
                    \.............................../
               hjw_,~')_,~')_,~')_,~')_,~')_,~')_,~')/,~')_

ship name : 
""")
            if ship == "WWS" :
                print("""Correct choice. look what you found ;
      __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|


""")
            elif ship == "HJW" :
                print("""Bumm 
              ..-^~~~^-..
                                .~           ~.
                               (;:           :;)
                                (:           :)
                                  ':._   _.:'
                                      | |
                                    (=====)
                                      | |
-O-                                   | |
  \                                   | |
  /\                               ((/   \))
    __    __    __
                             |==|  |==|  |==|
                           __|__|__|__|__|__|_
                        __|_________________|___
                     __|__[]__[]__[]____[]__[]__|___
                    |............................o...
                    ............................./
               hjw_,~')_,~')_,~')_,~')_,~')_,~')_,~')/,~')_
            
            """)
            else :
                print("No ship and game over.")              
        else :
            print("there is no such vehicle.")
    elif door == 2 :
        print("""Your dead
                       ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#""")
    else :
        print("there is no such door")
elif way == "Red" :
    print("""Snake poisoned on the way :
     ___            
    ,-~-.`.          
   (* */_\`\         
  ` \"/___) )        
   . | \_( /         
 .   ^  \_\|         
  _______\_\   
  \~~~~~~~/ )   
   \ o `./ /   
    \ ` /`/          
    -\_/,`           
   (`(_)   _       / 
    \`|   ( ) _  _`| 
     \\\   /_(_)(_)| 
   _/ \.\_           
  `-._|).-`          
      (_    """)
else:
    print(""" The guard told you to start over :
              .
             /.\
             |.|
             |.|
             |.|
             |.|   ,'`.
             |.|  ;\  /:
             |.| /  \/  \
             |.|<.<_\/_>,>
             |.| \`.::,'/
             |.|,'.'||'/.
          ,-'|.|.`.____,'`.
        ,' .`|.| `.____,;/ \
       ,'=-.`|.|\ .   \ |,':
      /_   :)|.|.`.___:,:,'|.
     (  `-:;\|.|.`.)  |.`-':,\
     /.   /  ;.:--'   |    | ,`.
    / _>-'._.'-'.     |.   |' / )._
   :.'    ((.__;/     |    |._ /__ `.___
   `.>._.-' |)=(      |.   ;  '--.._,`-.`.
            ',--'`-._ | _,:          `='`'
            /_`-. `..`:'/_.\
           :__``--..\\_/_..:
           |  ``--..,:;\__.|
           |`--..__/:;  :__|
           `._____:-;_,':__;
            |:'    /::'  `|
            |,---.:  :,-'`;
            : __  )  ;__,'\
            \' ,`/   \__  :
            :. |,:   :  `./
            | `| |   |   |:
            |  | |   |   ||
            |  | |   |   ||
            |  | |   '   ||
            |  : |    \  ||
            |  ; :    :  ||
            | / ,;    |\,'`.
            ;-.(,'    '-._,-`.
          ,'-.//          `--' 
          `---'
""")
