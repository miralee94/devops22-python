class Person:
    def __init__(self, name, birthyear) -> None:
        self.name=name
        self.birthyear=birthyear
    
    def __str__(self):
        return f" {self.name} {self.birthyear}"

    def printall(self):
        return print(f"Return stuff: {self.name} {self.__dict__}")


class Player(Person):
    def __init__(self, name, birthyear, speed, agility, strenght) -> None:
        super().__init__(name, birthyear)
        self.speed=speed
        self.agility=agility
        self.strenght=strenght
       
    def __str__(self) -> str:
        return f"Player: {self.name} Birthyear: {self.birthyear} Speed:{self.speed} Agility: {self.agility} Strenght: {self.strenght}"

class Coach(Person):
    def __init__(self,name, birthyear, voice_level) -> None:
        super().__init__(name, birthyear)
        self.voice_level=voice_level

class Team:
    def __init__(self) -> None:
        self.coach=None
        self.players=[]
    
    def add_player(self, player):
        return self.players.append(player)

    def switch_coach(self, coach):
        self.coach=coach
 
    def __str__(self):
        return self.players
        #return f"{[i.name for i in self.players]} {self.coach}"

    def print_team(self):
        return [print(i) for i in self.players]
        #return_string = ""
        #for x in self.players:
        #    return_string += f"{x}\n"
        #return print(return_string)

if __name__=='__main__':
    player1=Player("Thomas", "1993", "1-10", "1-10", "1-10")
    #print(player1)

    player2=Player("maja", "1993", "1-10", "1-10", "1-10")
    #print(player2)

    player3=Player("molly", "1993", "1-10", "1-10", "1-10")
    #print(player3)


    coach1=Coach("Leo", "1965", "1-10")
    #coach1.printall()

    team1=Team()
    team1.add_player(Player("Thomas", "1993", "1-10", "1-10", "1-10"))
    team1.add_player(player2)
    team1.add_player(player3)


    team1.switch_coach(coach1)
    
    #print(team1)
    team1.print_team()