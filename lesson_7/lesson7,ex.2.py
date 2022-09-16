
#1. Create a function that prints 1 to 10 by default, i.e `start=1` `stop=11` and uses a range in the function block.

def numbers(start=1, stop=11):
    return(list(range(start, stop)))
print(numbers())

#2. Create a function that by default prints a string, if `reverse=True` is used as argument the string is printed in reverse.

def rev(word, reverse=False):
    if reverse:
        word=word[::-1]
    print(word)

#3

rev("Hello", reverse=True)
rev("hello")