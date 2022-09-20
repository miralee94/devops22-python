from math import pi

class Circle:
    def __init__(self, diagonal) -> None:
        self.diagonal=diagonal
        self.color="grey"
    
    def area (self) -> None:
        return pi*(self.diagonal/2)**2
    
    def circumference (self):
        return 2*pi*(self.diagonal/2)
    
    def my_circle_set_color (self, color):
        self.color=color
  
if __name__=='__main__':
    cirkel1=Circle(5)
    print(cirkel1.area(), cirkel1.circumference(), cirkel1.my_circle_set_color("red"), cirkel1.color)





























































