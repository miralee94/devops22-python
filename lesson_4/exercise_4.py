#Exercise 1
#1 Ask the user for a integer
integer = int(input("Write a integer:"))
#2 If the integer is even, print even
#3 If the integer is odd, print odd
if(integer%2==0):
   print("even")
else:
    print("odd")

#Exercise 2
#Ask the user for a name
name=(input("What's your name? "))
#2 Create a tuple with at least five names
tuple_with_names=("Molly", "Maja", "Lars","Åke","Mira")
#3 If the user input is in the tuple, print the text "Welcome {name} your are on the list"
filter_name = list(filter(lambda x: x == name, tuple_with_names))
if len(filter_name) == 1:
    print(f"Found you {filter_name[0]}")
else:
    print(f"Did not find {name}")


if name in tuple_with_names:
    print(f"Welcome {name} your are on the list")
else:
    print("Hejdå")

found=False
for tuple_name in tuple_with_names:
    if(name==tuple_name):
        print(f"Welcome {tuple_name} your are on the list")
        found=True
        break
    else:
        found=False
if found==False:
    print(f"Sorre, you are not on the list")
    
#4 If the user input is not in the tuple, print "Sorry, you are not on the list"
else:
    print("Sorry, you are not on the list")

#Exercise 3
#1 Ask yhe user for a word
word=(input("write a word: "))
#2 Print the word x times, where x = len(word). i.e. if the word `hello` the program writes:
x=len(word)
print(word*x)

#Exercise 4
#1 Ask the user for a start and stop integer
start=int(input("Start integer "))
stop=int(input("Stop integer "))
#2 Print every integer between start and stop.

for i in range(start,stop):
    print(i)

#3 Print the sum of all integers
sum=start+stop
print("Sum:",sum) 

#Exercise 5

while True:
    my_input = input("Enter stop to quit: ").lower()
    if my_input == "stop":
        break
    else:
        print(my_input)
        print(len(my_input))