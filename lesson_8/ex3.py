

def funktion(x,y):
    try:
        print(type(x))
        if type(x) is not int or type(y) is not int:
            raise TypeError("It is not int")
        return x/y
    except ZeroDivisionError:
        print("Division by zero is not allowed")
    

print(funktion(5,5))