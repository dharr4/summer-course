# # # #review problems
# # # define a function and use it. a creative label. label/write the code, and call it.

# # import random
# # game_list = ['rock, paper, scissors']

# # print('Welcome to rock, paper, scissors. Choose one. Remember, I have better things to do so I wont play long. ')
# # user_choice = input('now choose. ')

# # comp_choice = random.choice(game_list)
# # if user_choice != game_list:
# #     print('Make a valid choice. ')

# # def game(user_choice:str, comp_choice:str):
# #     counter = 1
# #     while user_choice != comp_choice:

# #         if user_choice == 'rock' and comp_choice == 'scissors':
# #             print('You won that one.')
# #             counter += 1
# #         elif user_choice == 'rock' and comp_choice == 'paper':
# #             print('I won')
# #             counter += 1
# #         elif user_choice == 'paper' and comp_choice == 'scissors':
# #             print('I won')
# #             counter += 1
# #         elif user_choice == 'paper' and comp_choice == 'rock':
# #             print('You won')
# #             counter += 1       
# #     else:
# #         print('we tied!')
# #     if counter > 9:
# #         return 'Im donzo. '


# # principle = float(input('What is your principle? '))
# # rate = float(input('What is your rate? '))
# # timesyear = bool(input('number of times per year? '))
# # years = float(input('How many years'))

# # # amount = principle(1 + (intratedec/numoftimesintoveryear) ** time in years)
# # #try to use functions to solve

# # rateyear = rate / timesyear + 1
# # princrateyear = principle * rateyear
# # amount = princrateyear ** years

# # print(amount)

# ####Instructor solution####

# # def money(principle:float, interest:float, t: int, n:int = 1) -> float:
# #     return principle * (1 + interest/n) ** (n * t)

# # print(money(1000, 0.0061, 10, 1))

# # # def comp_int (rate:bool, timesyear:bool):
# # #     rate / timesyear:

# # import random

# # def fifty (number):
# #     counter == 0
# #     while counter == 0:
# #         random.randint(50, 100)
# #         print(number)
# #         counter + 1
# #     if counter  == 50:
# #         return number
    

# # random_number = random.randint(50, 100)
# # random_numbers = str(random_number)

# # print(random_numbers * 50)

# # with open('testfile.txt', 'r') as file:
# #     lines = file.readlines()
# #     for line in lines:
# #         print(line)

# # with open('testfile.txt', 'r') as file:
# #     lines = file.readline()
# #     for lin

# ###########instructor example########

# import random
# with open('file.txt', 'w') as file:
#     for line in range(100):
#         random_number = random.randint(50, 100)
#         file.write(str(random_number) + '\n')

# with open('file.txt', 'r') as input_file:
#     lines = input_file.readlines()
#     # print(lines)
#     # for line in lines:
#     #     print(line)
#     count = 0
#     min = 1000
#     max = 0
#     min = 0
#     for line in lines:
#         amount = int(line)
#         sum += amount
#         count += 1
#         if amount > max:
#             max = amount
#         if amount < min:
#             min = amount
# average = sum / count

# print(f' max: {max} min: {min} average: {average}.' )


#new module. the os module. to interface with the underlying os
#import os
#os.mkdir, os.listdir, os.path.join

import os
print(os.getcwd())