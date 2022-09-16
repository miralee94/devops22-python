from math import pi

class Circle:
    def __init__(self, diagonal, color="grey") -> None:
        self.diagonal=diagonal
        self.color=color
    
    def area (self) -> None:
        return pi*(self.diagonal/2)**2
    

    def circumference (self):
        return 2*pi*(self.diagonal/2)
    
    def my_circle_set_color (self, color):
        self.color=color


    
    def __init__(self) -> None:
        self.diagonal=10
        print(self.area(), self.circumference())
if __name__=='__main__':
    cirkel1=Circle(5)
    print(cirkel1.area(), cirkel1.circumference(), cirkel1.color)





























































