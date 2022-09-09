#exersice 1, Basic usage
#1. Print first, lastname and tele on the same line
firstname = "john"
lastname = "smith"
tele = "00468123456789"

print(firstname,lastname,tele)
#2. Create a variable fullname
fullname=(firstname+lastname)
#3. Assign to the new variable fullname, firstname and lastname separated with a space.
fullname2=(firstname+" "+lastname)
print(fullname2)
#4. Print the length `len()` of fullname, firstname and lastname
print(len(fullname))

#5. Print a escape sequence `\n` so the first line contains fullname, and the second line tele.
print(firstname, lastname, f"\n"+tele)
#6. Write the fullname and tele with the four different methods:
#1. Only using print() and string concatenation i.e "firstname" + " " ..
print(firstname,lastname,tele)
#2. Using f-string
print(f"jonh smith 00468123456789")
#3. Using format, i.e print('{}'.format(firstname))
print("{} {}".format(fullname2, tele))
#4 Using print f (%) syntax, i.e print('A name %s' % firstname)


#Exercise2_slice
#1. Use slice to get the first 5 characters i fullname
print(fullname[0:5])
#2. Use slice to get all characters except the first and last one
print(fullname[1:8])
print(fullname[1:-1])
#3. Use slice to get every other character, i.e abcdef would print ace. Print the result in uppercase.
print(fullname[::2])
#4. Use slice to print a word backwards.
längden=len(fullname)
slicedfullname=fullname[längden ::-1]
print(slicedfullname)
#5. Use slice to get the 5th character
print(fullname[4])

#3 Unicode
#1. Let the user input a price, i.e Your new car cost: 1000000
price=int(input("Price: "))
#2. Add a currency symbol (not dollar) to the input string. ie. Your new car cost [$]
print("Your price is",price, "\u20AC")
#3. Depending on the price, respond with a matching emoji (you decide which ones) i.e if cost below 50000 use one emoji, if is above another one
if price < 100:
    print("\U0001F600")
else:
    print("\U0001F607")

#4 Extra
#1. The boss tells the user it's current salary and currency
#2. The employee ask for more money with an input. I.e 2000 more
#3. The boss calculates the percentage salary increase and respond with a emoji. And always respond NO to the initial proposal.
#4. The employee ask again for another amount i.e 1800
#5. The boss calculates the percentage and respond yes or no, you decide which criteria the boss uses. 
# 4 and 5 iterates in a loop until the employee quit or the boss accept the amount.


original_salary = 3500
print(f"Boss: your current salery is: \u0024{original_salary}: ")
tries = 0
while True:
    employee_increase = int(input("Employee: I want more moneyyyyy, give me this much increase: "))
    increase_percentage = round((employee_increase /  original_salary) * 100, 2)

    if tries == 0:
        print(f" Boss: \U0001F607 Your increase of {increase_percentage}% is DENIED, try again")
    elif increase_percentage > 3.0:
        print(f" Boss: \U0001F607 It's still too much {increase_percentage}% try again")
    elif increase_percentage < 3.0:
        print(f"Boss: incease of {increase_percentage}% is accepted, your new salary will now be \u0024{original_salary + employee_increase}")
        break
    if tries == 4:
        print("You are fireeeed! ")
    tries += 1


