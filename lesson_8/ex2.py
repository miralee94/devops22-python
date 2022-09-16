#1. Create a program that takes input and convert it to a integer
number=None
while number != int:
    try:
        number=int(input("skriv ett tal: "))
        if number%2==0:
            print("Not allowed")
        else:
            print("Allowed")
            break
#2. If it's not possible to convert it to a integer the program should print `Sorry, not an int`
    except ValueError:
        print("Sorry, not an int")

#3. If the input fail to convert to a int, the program should retry the input


