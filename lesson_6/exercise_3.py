from queue import Empty
import string
from operator import mul
from random import shuffle, choices, sample
from typing import Counter

# 1. Generate a list of lowercase a-z
alphabet = list(string.ascii_lowercase)
print(alphabet)

#2. Iterate through the alphabet and append each letter to a stack
stack = []
for letter in alphabet:
    stack.append(letter)
print(stack)
#3. Pop all elements and print on one line as a string

sträng = ""
    
while stack:
    sträng += stack.pop()
print(sträng)