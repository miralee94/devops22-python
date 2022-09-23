class Cat():
    
    def say_mjau():
        return "Cat says mjau"

class Kittycat(Cat):

    def say_mjau():
        return "Kittycat says mjau"

if __name__ == "__main__":
    print(Cat.say_mjau())
    print(Kittycat.say_mjau())
    
