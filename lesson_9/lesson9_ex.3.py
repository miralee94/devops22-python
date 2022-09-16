#skapar class
class Square:
#med 1 argument
    def __init__(self, side) -> None:
        self.side=side
#1 metod
    def area(self):
        return float(self.side**2)
#2 metod   
    def cirkumference(self):
        return float(self.side*4)
 
    def __init__(self, side) -> None:
        self.side=2

    def __init__(self, side) -> None:
        self.side=3.5
           

if __name__=='__main__':
    square1=Square(2)

    square2=Square(3.5)
    
    print(square1.area(), square1.cirkumference())
    print(square2.area(), square2.cirkumference())
   