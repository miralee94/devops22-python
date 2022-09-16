class Animal:
    def __init__(self, breed) -> None:
        self.breed = breed
    
    def __str__(self) -> str:
        return f"{self.breed} {self.__dict__}" 
    


class Dog(Animal):
    def __init__(self, breed, name, age) -> None:
        super().__init__(breed)
        self.name = name
        self.age = age

class Supermarket:
    def __init__(self, name, land, storlek) -> None:
        self.name=name
        self.land=land
        self.storlek=storlek
    def __str__(self) -> str:
        return f"{self.name} {self.__dict__}"

class Coop(Supermarket):
    def __init__(self, chef, anställda, öppettider, adress) -> None:
        super().__init__("Coop", "Sverige", "222kvm")
        self.chef=chef
        self.anställda=anställda
        self.öppettider=öppettider
        self.adress=adress

print(Coop("dfs", 45, "8-21","df"))







