#morning exercise

import random
with open('numbers.txt', 'w') as file:
    for line in range(100):
        random_numbers = random.randint(1, 1000)
        file.write(str(random_numbers) + '\n')