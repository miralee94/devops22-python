# Exercise 1 Dataset
from audioop import add
from operator import mul
from random import shuffle, choices, sample
from typing import Counter
#1. Generate a list containing the numbers 1, 2, 3 to 100.
one_to_hundred=list(range(1,101))
print(one_to_hundred)

#2. Generate a list of all even numbers from 2 to 60
even_numbers=list(range(2, 61 , 2))
print(even_numbers)
# 3. Generate a list of all odd numbers from 1 to 77
odd_numbers=list(range(1, 78, 2))
print(odd_numbers)
#4. Generate a list of 100 numbers between 1 - 300
tal=list(range(1,301))
#4.1
unique_numbers=(sample(tal, k=100))
print(unique_numbers)
#4.2
numbers=(choices(tal, k=100))
print(numbers)

#5 create a list containing five colors (not containing red)
colors=["green", "gray", "black", "white", "blue"]
#5.1 Create a new list containing "red" and also add two colors by random with `choice`, `choices` or `sample` from the list.
new_color_list=["red"]
pick_two=choices(colors, k=2)
new_color_list=new_color_list.__add__(pick_two)
print(new_color_list)

new_color_list.extend(sample(colors, k=2))
print(new_color_list)
#5.2 Generate a list of random colors from the list of 3, the list should be of length 50.
pick_fifty=choices(new_color_list, k=50)
print(pick_fifty)
#5.3 Print the length of all three lists and the unique colors in each list
print(f"{len(pick_fifty)} {len(new_color_list)} {len(colors)}")
new_color_list=pick_fifty.__add__(new_color_list)
new_color_list=colors.__add__(new_color_list)
print(new_color_list)
unique_colors=set(new_color_list)
print(unique_colors)