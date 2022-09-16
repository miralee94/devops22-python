#Create a function that check if a variable is a float, if not it raises a TypeError("message")

try:
    float("hej")
except ValueError:
    print("Det är inte decimal")

floatttt=[1.0]
try:
    float(floatttt)
except TypeError:
    print("fel")