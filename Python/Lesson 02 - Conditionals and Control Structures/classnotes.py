#Notes from class
#Python best used for data extraction and manipulation. A high level language.
#Good for visualization and data loading into a database for our own use.
# Data exploration; Panda
#Explore data, look for patterns and trends, data modeling, AI modeling scikitlearn and pytorch.
# backend development, flask and fastAPI, jango and react

#conditional statements: else; if; elsif. useful with comparison operators and logical operators.
#python relies on indentation

# age = 20
# if age >= 20:
#     print ("eligible")

# elif is short for else if. checks multiple conditions. 
#if condition:
    #code
#elif condition:
    #code
#else condition:
    #code

#Check for even and odds globally:
# num %2 ==0 or num %2 ==1
#this checks the number if divisible by 2 or 1

# definitive loop is defined by running for a number of iterations == FOR LOOP
# WHILE LOOP = run infinite

#new data type == LIST uses [ ]. elements in list sepreated by commas. Stores multiple data types.
# mylist = ['hello', 5, True]

# range == similiar to a list. generates a list. range(5) will generate 0,1,2,3,4

# range(2,7) this is a start, stop value. 2,3,4,5,6

# range also uses the start,stop,step

# builds up to loops
#for loops and while loops
#keyword FOR variable IN sequence:
#example print umbers from 1 - 10
#a loop variable only exists inside the loop.

# for number in range(1,11):
#     print(number)

# number will retain the last value assigned to it. the loop can assign to variables. Be careful how they are named. 
# can use my_name_list.index('david') this will search the list and give you the index the value is at.
# my_name_list.sort() will make it alphabetical

# my_name_list = ['bob', 'jack', 'ryan']
# my_name_list.append('david')
# print(my_name_list)

# for number in range(20,51,2):
#     print(number)
#prints numbers 20-50, only even numbers.

# for number in range(20-51):
#     if number % 2 == 0

## while loops
#while condition
#   block of code


secret_num = 22

user_guess = int(input("Guess a whole number. "))

count = 1

while user_guess != secret_num:
    if count > 5:
        break
    if user_guess < secret_num:
        print("your guess is too low.")
    else:
        print("your guess is too high")
    user_guess = int(input("Guess a whole number. "))
    count += 1
if user_guess == secret_num:
    print(f"yay you guessed the right number after {count} tries, {user_guess}!")
else:
    print("better luck next time.")
