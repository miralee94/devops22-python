
#exercise_3

x = True
y = False
z = True

#1.1

if x or y or z is True:
    print(True)

#1.2 and 1.3
if x and y and z is True:
    print(True)
else:
    print(False)
#1.4 and 1.5
if x and y and z is False:
    print(False)
elif x or y or z is True:
    print(True)
#1.6 
if x and y and z is True:
    print(False)

'''
Uppgift A

1. Numeric types
2. dict
3. print (addresses ["Bella"])
4. Daniel addas till dict (addresses)
5. print(len(addresses))
5.1 lastkey = list(addresses.keys())[-1]
print(addresses[lastkey])
5.2 firstkey = list(addresses.keys())[0]
print(firstkey)
6. List
7. Opel
8. IndexError: list index out of range
9. BMV
10. cars utökas, eftersom cars2=cars är variablernas innehål identiskt?
10.1 cars_3 = tuple(cars)
cars.append ("Porsche")
print (cars)
print (cars_3)
10.2 reversed_cars = sorted(cars)
merged = cars + reversed_cars
print (merged)
or
reversed_cars = sorted(cars)
cars.extend(reversed_cars)
print (cars)
10.3 unique_cars = set(merged)
print(unique_cars)
11. print(type(numbers2)) set
12.
13. numbers3 = numbers1.intersection(numbers2)
print (numbers3)
14. set_union = numbers1.union(numbers2)
print (set_union)
15. numbers1.symmetric_difference_update(numbers2)
print (numbers1)
'''
#Uppgift B
