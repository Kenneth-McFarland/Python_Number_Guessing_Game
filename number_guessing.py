print('Welcome to number guessing!')
import random
number_to_guess = random.randint(1,999)
guessed_number = ''
while guessed_number != number_to_guess:
    guessed_number = int(input('What do you think the correct number is? '))
    if guessed_number < number_to_guess:
        print('Higher!')
    elif guessed_number > number_to_guess:
        print('Lower!')
    else:
        print(f'Great job! The answer was {number_to_guess}.')