# -*- coding: utf-8 -*-
import string, random

# Ask user for input
letter_input_1 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter OR enter a specific letter: ')
letter_input_2 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter OR enter a specific letter: ')
letter_input_3 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter OR enter a specific letter: ')
letter_input_4 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter OR enter a specific letter: ')
letter_input_5 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter OR enter a specific letter: ')

# According to user input, generate five letters.
vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = string.ascii_lowercase

def generator():
    # Generate letter 1
    if letter_input_1 == "v":
        letter1 = random.choice(vowels)
    elif letter_input_1 == "c":
        letter1 = random.choice(consonants)
    elif letter_input_1 == "l":
        letter1 = random.choice(letters)
    else:
        letter1 = letter_input_1 # User's specific input
        
    # Generate letter 2
    if letter_input_2 == "v":
        letter2 = random.choice(vowels)
    elif letter_input_2 == "c":
        letter2 = random.choice(consonants)
    elif letter_input_2 == "l":
        letter2 = random.choice(letters)
    else:
        letter2 = letter_input_2 # User's specific input
        
    # Generate letter 3
    if letter_input_3 == "v":
        letter3 = random.choice(vowels)
    elif letter_input_3 == "c":
        letter3 = random.choice(consonants)
    elif letter_input_3 == "l":
        letter3 = random.choice(letters)
    else:
        letter3 = letter_input_3 # User's specific input
        
    # Generate letter 4
    if letter_input_4 == "v":
        letter4 = random.choice(vowels)
    elif letter_input_4 == "c":
        letter4 = random.choice(consonants)
    elif letter_input_4 == "l":
        letter4 = random.choice(letters)
    else:
        letter4 = letter_input_4 # User's specific input
        
    # Generate letter 5
    if letter_input_5 == "v":
        letter5 = random.choice(vowels)
    elif letter_input_5 == "c":
        letter5 = random.choice(consonants)
    elif letter_input_5 == "l":
        letter5 = random.choice(letters)
    else:
        letter5 = letter_input_5 # User's specific input
    
    name = letter1 + letter2 + letter3 + letter4 + letter5
    
    return(name)

print(generator())