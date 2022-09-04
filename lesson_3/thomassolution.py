
my_list = list()

name_1 = input("Please enter name for person 1: ").lower()
age_1 = input("Please enter age for person 1: ")
shoe_size_1 = input("Please enter shoe size for person 1: ")

name_2 = input("Please enter name for person 2: ").lower()
age_2 = input("Please enter age for person 2: ")
shoe_size_2 = input("Please enter shoe size for person 2: ")

name_3 = input("Please enter name for person 3: ").lower() 
age_3 = input("Please enter age for person 3: ")
shoe_size_3 = input("Please enter shoe size for person 3: ")

my_list.append((name_1, age_1, shoe_size_1))
my_list.append((name_2, age_2, shoe_size_2))
my_list.append((name_3, age_3, shoe_size_3))

oldest = sorted(my_list, key=lambda x: x[2], reverse=True)
print(f"The oldest person is {str(oldest[0][0]).capitalize()} who has shoe size {oldest[0][2]}")

sorted_shoes = sorted(my_list, key=lambda x: x[2])

median_shoe_size = sorted_shoes[1] #Since it's always 3, no need to calculate median

print(f"The person with median shoe size is {str(median_shoe_size[0]).capitalize()} who is {median_shoe_size[1]} years old")


term, value = input("Please enter search value, name, age or size followed by value: ").lower().split(" ")

search_map = {
    "name": 0,
    "age": 1,
    "size": 2}

index = search_map[term]

result = list(filter(lambda x: x[index] == value, my_list))
print(f"Found person \nName: {str(result[0][0]).capitalize()}\nAge: {result[0][1]}\nSize: {result[0][2]}")