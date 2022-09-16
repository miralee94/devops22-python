
import string
#1 
def do_nothing():
    pass
do_nothing()

#2.1
def greeting():
    print("hello world")
greeting()
#2.2
def result():
    print(1==1.0)
result()
#2.3
def alphabet():
    print(string.ascii_lowercase[::-1])
alphabet()
#3.1
name=input("What is your name? ")
def hälsning():
    print(f"Hello, {name}")
hälsning()
#3.2
word="word"
def min_funktion():
    print(str.upper(word))
min_funktion()

def cap(word):
    print(word.upper())
cap("Mira")
#3.3
def numbers(stop):
    return(list(range(1,stop)))
print(numbers(20))

