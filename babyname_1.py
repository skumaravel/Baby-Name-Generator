# Importing string module to reuse functions and constants from it
import string

print(string.ascii_letters)
print(string.ascii_lowercase)

# Importing random module because we are going to randomly generate names.
import random
print(random.choice(string.ascii_letters))