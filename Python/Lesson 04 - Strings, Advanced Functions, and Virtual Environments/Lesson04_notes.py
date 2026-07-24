# # my_list = ['c', 'a', 't']

# # my_string = 'cat'

# # for char in my_string:
# #     print(char)

# # for char in my_list:
# #     print(char)



# # print(my_list[0], my_string[0])

# # print(my_list[-1], my_string[-1])

# # print(my_string[0:2])

# # print(len(my_list), len(my_string))

# # #lists can be changed, strings cannot. keyword is mutable and immutable. if you want to replace one of the values.

# #validate username. between 5-15 char. returns true if valid, or false if otherwise. only contain letters, digits, underscores. 
# #start wth letter, not end with underscore, contain one digit.

# # username = input('Enter a username. ')

# # def validate_username(username):
# #     username_len = len(username)
# #     if username_len > 15:
# #             return 'False'
# #     if username_len < 5:
# #             return 'False'
# #     else:
# #         for letter in username:
# #             if letter == digit:
# #                 hasDigit = True
# #             if letter == letter.upper:
# #                 hasuppercase = True
    

# # print(username_len)
# #instructor solution

# #define a function that validates a username based on requirements.

# def validate_username(username :str) -> bool:
#     length_req = False
#     num_letters_underscores = False
#     hasDigit = False

#     username_length = len(username)
#     if username_length > 5 and username_length < 15:
#         length_req = True

#     for char in username:
#         if not(char.isalnum() and char == '_'):
#             num_letters_underscores = False
#     if username[0].isalpha():
#         starts_with_letter = True

#     if char in username:
#         if char.isdigit():
#             hasDigit = True

# #assert statement assert validate_username('david42069') == True
# #assert validate_username('bill') == False


#modules. built in, your own that are written, or 3rd party pip install.

#created functions in area.py and called them in main.py

# def greet(name, greeting='Hello'):
#     print(f'{greeting}, {name}!')

# #functions can have multiple returns.

# def min_max(numbers):
#     return min(numbers), max(numbers)

passengers = ['Lopez', 'Chen', 'Okafor', 'Smith', 'Patel']

# def print_boarding_list(passengers):

for index, passengers in enumerate(passengers, 1):
    print(f'Passenger {passengers} in seat {index}')

colors = ["red", "green", "blue"]
for index, color in enumerate(colors, start=1):
   print(f"Color {index}: {color}")