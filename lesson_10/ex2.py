class Dog():

    def __init__(self, breed, age, gender) -> None:
        self.breed = breed
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.breed}, {self.age}, {self.gender}"

class Menu():

    def start_menu():
        running = True
        while running == True:
            choise = input ("""Hello, welcome to menu: 
            1) Create the object 
            2) Print the object
            3) Delete a object 
            """)

            if choise == "1":
                dog = Dog("Husky", "2 years old", "Male")
                print(dog)
            if choise == "2":
                try:
                    print(dog)
                except:
                    print("No object available to print")
            if choise == "3":
                try:
                    del dog
                    print("Dog deleted")
                except:
                    print("No object to delete")


Menu.start_menu()


    
