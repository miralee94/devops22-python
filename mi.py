class Animal:
    def __init__(self, typ):
        self.typ=typ
       
    def __str__(self):
        return f"{self.typ} {self.__dict__}"
        
class Dog(Animal):
    def __init__(self, typ, name, age):
        super().__init__(typ)
        self.name=name
        self.age = age


class Supermarket:
    pass

class Coop:
    pass

hund1=Dog("Husky", "Maja", 2)
print(hund1)