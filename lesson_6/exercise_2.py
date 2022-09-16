from audioop import reverse
from genericpath import samefile
import string
from operator import mul
from random import random, shuffle, choices, sample
from typing import Counter

#1. Generate a list with 100 elements, i.e ["johan", "lisa", "johan", "tove"...]
names=["johan","lisa","johan","tove","molly", "maja","nina","adam", "bertil", "caesar", "david", "erik",
         "filip", "gustav", "helge", "ivar", "johan"]
hundred_names = names * 100
sample_names = sample(hundred_names, k=100)
#2. Count the names i.e ('lisa', 1), ('johan',2)
print(Counter(sample_names).most_common())
#3. Print the top 3 most popular names
print(Counter(sample_names).most_common(3))
#4. Print the least popular name[s]
least_common = Counter(sample_names).most_common()[::-1][:3]
print(least_common)
#5. Print all unique names
    #1. In alphabetical order
unique_names=set(sample_names)
print(unique_names)
    #2.Shuffled
unique_names=list(unique_names)
shuffle(unique_names)
print(unique_names)
    #3. In reversed alphabetical order
unique_names.sort(reverse=True)
print(unique_names)
