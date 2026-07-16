
# # #generate numbers 1-100. If divisible by 3 print buss, if by 5 print fizz. if by both print fizzbuzz.

# # for numbers in range(1,101):
# #     if numbers / 3 and 5:
# #         print("FizzBuZZ")
# #     if numbers / 3:
# #         print("buzz")
# #     if numbers / 5:
# #         print("fizz")
# #     else:
# #         print(numbers)
    

    
# # #% 3 == 0 and % 5 == 0 TRY this code instead

# #ask user for rock, paper, scissors. randomly assign computer choice of rock paper scissors. display won, lost, draw.


# #***************************************#
# #import random
# # random_number = random.randit()


# # computer_choice = "rock"
# # user_choice = input("choose rock paper or scissors. ")

# # if user_choice == "rock" and computer_choice == "rock":
# #     print("Draw")
# # elif user_choice == "rock" and computer_choice == "scissors":
# #     print("you win")


# #guessing game. randomly assign 1-100 using the random module. ask user to guess. then too high, too low, then correct. 

# secret_num = 50

# user_guess = int(input("Guess a number between 1 and 100." ))

# count = 1

# while user_guess != secret_num:
#     if count > 5:
#         break
#     if user_guess < secret_num:
#         print("your guess is too low.")
#     else:
#         print("your guess is too high")
#     user_guess = int(input("Guess a whole number. "))
#     count += 1
# if user_guess == secret_num:
#     print(f"yay you guessed the right number after {count} tries, {user_guess}!")
# else:
#     print("better luck next time.")


# import random
# random_number = random.randint(1,100)
#import numpy as np

#modules == libraries. python calls them modules.

# import random
# random_number = random.randint(0,100)

# print(random_number)

# if random_number < 50:
#     print("This number is less than 50.")
# elif random_number > 50:
#     print("This number is greater than 50.")
# else:
#     print("This number is 50.")

#create a definition, then CALL the function to execute.
#define function by def. add paramters. follow :
    #function code or function body
    #return statement
#function call is call the function_name (arguments, arguments)

# def add_together(num1, num2):
#     sum = num1 + num2
#     return sum
# result1 = add_together(10, 20)

# print(result1)

#write a python statement that calc and returns the area of a rectangle using two int (L*W) 


# def area_calc(len: int, wid: int):
#     prod = len * wid
#     return prod
# result1 = area_calc(10, 10)

# print(result1)

# #ask user unput for length and width

#write a fun called tip with 2 parameters total and percentage.
# create a few tip calculators#
# def tip(total: float, percentage: int):
#     bill = total / percentage
#     return bill

# cust_bill = float(input("What was the bill?"))
# cust_tip = int(input("What will you tip?"))
                     
                    
# result = tip(cust_bill, cust_tip)

# print(tip) 

#write fun called has_more_characters. accept two strings as arguments and return the string with more characters
#decorators to describe functions for other people to see

# string1 = input("Write some characters.")
# string2 = input("Write different characters.")


# def str_compare(str1: str, str2: str):
#     len1 = len(str1)
#     len2 = len(str2)
#     if len1 > len2:
#         return str1
#     elif len1 < len2:
#         return str2
#     else:
#         return "Equal"
    
#if len(string1) > len(string2)








