# -*- coding: utf-8 -*-
import string, random

# Function creating a randomly generated 5 letter name.
def generator():
    
    # Generate random letters
    letter1 = random.choice(string.ascii_lowercase)
    letter2 = random.choice(string.ascii_lowercase)
    letter3 = random.choice(string.ascii_lowercase)
    letter4 = random.choice(string.ascii_lowercase)
    letter5 = random.choice(string.ascii_lowercase)
    
    # Create a 5 letter string using the generated letters
    name = letter1 + letter2 + letter3 + letter4 + letter5
    
    return(name)

print(generator())

# Ask user for input
letter_input_1 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter OR enter a specific letter: ')
letter_input_2 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter OR enter a specific letter: ')
letter_input_3 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter OR enter a specific letter: ')
letter_input_4 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter OR enter a specific letter: ')
letter_input_5 = input('Choose a letter..."v" for vowels, "c" for consonants, "l" for any other letter OR enter a specific letter: ')
