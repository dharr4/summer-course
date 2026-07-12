# Pitt pizza show two for one deal. 
# small is 12 inch, two for 9.99
# Large is  17 inch for 9.99
# 3.14 for pi. A = pi * radius ** 2
# 

pizza_size = input("What is the size of your pizza in inches?" ) 
pizza_cost = input("What is the cost of that pizza?")

pizza_calc = float(pizza_cost)
pizza_diam = int(pizza_size)



print("Your pizza is", pizza_size ,"inches.") 
print("The cost per area of your pizza is", pizza_calc / (3.14 * (pizza_diam / 2) ** 2))