user_name = input("What is your name? ")

fav_num = input("What is your favorite number? ")

text_two = f"*  Your favorite number is {fav_num}  *"
text_one = f"*  Hello, {user_name}"
spaces = " " * (len(text_two) - len(text_one) - 1)
text_one += spaces+"*"
border_line = "*" * len(text_two)

print(border_line, "\n" + text_one, "\n" + text_two, "\n" + border_line)