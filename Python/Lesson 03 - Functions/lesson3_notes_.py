#Lesson 3 Class Notes
# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 5 == 0:
#         print("Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     else:
#         print(number)


# computer_choice = "rock"
# user_choice = input("Enter rock, paper, or scissors:  ")

# if user_choice == "rock" and computer_choice == "paper":
#     print("You Lose")
# elif user_choice == "rock" and computer_choice == "scissors":
#     print("You Win")
# elif user_choice == "paper" and computer_choice == "scissors":
#     print("You Lose")
# elif user_choice == "paper" and computer_choice == "rock":
#     print("You Win")
# elif user_choice == "scissors" and computer_choice == "rock":
#     print("You Lose")
# elif user_choice == "scissors" and computer_choice == "paper":
#     print("You Win")
# else:
#     print("You tie")


# import random

# random_number = random.randint(1,100)
# user_number = int(input("Enter a number between 1 and 100: "))
# count = 0
# num_guesses = 0
# while user_number != random_number and num_guesses < 5:
#     if user_number > random_number:
#         print("You guessed too high")
#     else:
#         print("You guessed too low")
#     user_number = int(input("Enter a number between 1 and 100: "))
#     count += 1
#     num_guesses += 1

# if num_guesses < 5:
#     print(f"Congratulations, you guessed {random_number}, and it took you {count} retries!")
# else:
#     print("Better luck next time.")



# from random import randint as ri

# random_number = ri(1,100)

# if random_number < 50:
#     print("The number is less than 50")
# elif random_number > 50:
#     print("The number is greater than 50")
# else:
#     print("The number is 50")

# print(random_number)

# def rect_area(len: int, wid: int) -> int: 
#     #Comments
#     return len * wid

# lenth = int(input("Enter the length:  "))
# width = int(input("Enter the width  "))

# area1 = rect_area(length, width)
# print(area1)


# def tip(total: float, percentage: float) -> float:
#     percentage_by_100 = percentage/100
#     tip_amount = total * percentage_by_100
#     return tip_amount

# print(f"The amount to tip is ${tip(100, 25)}")


# print(f"The amount to tip is ${tip(200, 50)}")

# length1 = input("Type some characters. ")
# length2 = input("Type some different characters. ")

# def has_more_characters(string1 : str, string2: str) -> str:
#     length1 = len(string1)
#     length2 = len(string2)
#     if len(string1) > len(string2):
#         return f"{string1} has more characters"
#     elif length2 > length1:
#         return f"{string2} has more characters"
#     else:
#         return "They are equal"
    
# longer_greeting = has_more_characters([length1, length2]) #([1,2,3], [1])

# print(f"{longer_greeting}")
    
# a_test_list = ['a, b, c']
# for item in a_test_list:
#     print(item)


# curr_temp = int(input('What is the temperature? '))
# rain_status = input('Is it raining? ')

# # if curr_temp > 65:
# #     print('Enjoy the weather!')
# # elif curr_temp > 40:
# #     print('Bring a jacket')
# # else:
# #     print('bring a coat')
# # if rain_status ==

# if curr_temp < 40:
#     output = "Bring a coat. "
# elif curr_temp <= 60:
#     output = 'Bring a jacket '
# else:
#     output = 'Enjoy the weather! '

# if rain_status == 'yes' :
#     output += "Bring an umbrella. "

# print(output)
##################################################
# start = int(input('Enter the start value '))
# stop = int(input('Enter the stop value '))

# def fizzbuzz(beginning: int, end: int) ->None:
#     counter = 0
#     for numbers in range(beginning,end+1):
#         if numbers % 3 == 0 and numbers % 5 == 0:
#             print('FizzBuzz')
#             counter += 1
#         if numbers % 3 == 0:
#             print('Fizz')
#         elif numbers % 5 == 0:
#             print('Buzz')
#         else:
#             print(numbers)
#     return counter
# amount = fizzbuzz(start, stop)

# print(f'there are {amount} of fizzbuzzes in between and including {start} {stop} ')

#password exercise

# user_password = input('Enter a password to test. ')

# if user_password > 8 and int == True:
#     print:('Strong')
# elif user_password > 8:
#     print('Medium')
# else:
#     print('Weak')


#instructor example
#
# digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# def password_checker(password: str) ->str:
#     password_len = len(password)
#     if password_len < 8:
#         return 'weak'
#     else:
#         for letter in password:
#             #check if the letter is equal to a digit
#             for digit in digit_list:
#                 if letter == digit:
#                     hasDigit = True
                    
#             if letter == letter.upper():
#                     hasuppercase = True

                    
#                     return 'strong'
#         return 'Medium'

# user_password = input('Enter a password ')
# password_strength = password_checker(user_password)

# while password_strength != 'strong':
#     print(f'The password strength is {password_strength}')
#     user_password = input('Enter a password ')
#     password_strength = password_checker(user_password)

# print(f'this password is {password_strength}, great job!')




########################################################

# num_of_test = input('How many test scores will you enter? ')
# test_scores = float(input('Enter the test scores. '))

# A = range(90, 100)
# B = range(80, 89)
# C = range(70, 79)
# D = range(60, 69)
# F = range(0, 59)

# def letter_grade

#instructor walkthrough

def letter_grade(score: float) ->str:
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    return 'F'

print(letter_grade(95))
print(letter_grade(85))
print(letter_grade(75))
print(letter_grade(65))
print(letter_grade(55))
students = int(input('How many grades are there to enter? '))
total_scores = 0
for student in range(1, students+1):
    score = float(input(f"Enter students #{student}'s score:  "))
    total_scores += score
    print(f"Student #{student} got a letter grade {letter_grade(score)}")

print(f"The class average was {total_scores/students}, this is a {letter_grade(total_scores/students)}")