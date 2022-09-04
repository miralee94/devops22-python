#exercise_3
from audioop import reverse
from unittest.util import sorted_list_difference


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

    #exercise 4
#1
my_empty_list=[]
#2
pinkcolor = "pink"
#3
my_empty_list.append(pinkcolor)
#4
print(my_empty_list[0])

#5
my_empty_list += ["red", "greem"]
print(my_empty_list)
#6
print("red" in my_empty_list)
#7
print("yellow" not in my_empty_list)
#8
my_new_list = ["yellow", "black", "white"]
my_newest_list=my_empty_list + my_new_list
print(my_newest_list)
#9
my_color_list = ["red","yellow"]*3
print(my_color_list)
#10
print(my_color_list[0:4])
#11
print(my_color_list.count("red"))
#12
print(my_color_list.index("yellow"))
#13
print(len(my_color_list))
#14
list_of_7_numbers = list(range(1,8))
print(list_of_7_numbers)
#14.1
print(min(list_of_7_numbers))
#14.2
print(max(list_of_7_numbers))

#exercise_5
cars=["volvo","kia","bmw","ford", "citröen","volkswagen","mercedes", "audi","toyota","renault",]
#5.1 and 5.3
print(sorted(cars))
print(sorted(cars, reverse=True))

#5.2 and 5.3
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

#5.4
list_of_10_tuples=[("volvo","xc90"),("kia","5000"),("bmw", "m5"),("ford","mustang"),("volkswagen", "golf"),("mercedes","s-class"), ("citröen", "C7"),("audi","r8"),("toyota","supra"),("renault","zoe")]
print(list_of_10_tuples)
sorted_by_brand = sorted(list_of_10_tuples, key=lambda x: x[0])
print(sorted_by_brand)

sorted_by_model=sorted(list_of_10_tuples, key=lambda x:x[1])
print(sorted_by_model)