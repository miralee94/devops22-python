class Boll:
    pass

class Fotboll(Boll):
    pass


print(issubclass(Fotboll, Boll))
print(Boll.__subclasses__())
print(Fotboll.__bases__)

class Shape:
    def __init__(self, name):
        self.name=name

    def __str__(self) -> str:
        return f"{self.name} {self.__dict__}"

class Rectangle(Shape):
    def __init__(self, b, l):
        super().__init__("Rectangle")
        self.b=b
        self.l=l
    
    def area(self):
        return self.b * self.l

rect=Rectangle(2,3)
print(rect.area())
print(rect)