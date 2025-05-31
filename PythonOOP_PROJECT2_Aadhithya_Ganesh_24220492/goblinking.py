from goblin import Goblin
from archer import Archer

class GoblinKing(Goblin, Archer):
    # Constructor to initialize the stats for the goblin king. 
    # We can set the name, hp, maxHP and abilities by calling the super class constructor of goblin.
    # Also set an isEmpowered instance variable.
    def __init__(self, name, maxHP = 50):
        Goblin.__init__(self, name, maxHP)
        self.isEmpowered = False
