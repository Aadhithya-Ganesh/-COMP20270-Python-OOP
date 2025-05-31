from creature import Creature

class Goblin(Creature):
    # Constructor to initialize the stats for the goblin. 
    # We can set the name, hp and maxHP by calling the super class constructor of creature
    def __init__(self, name, maxHP = 15):
        Creature.__init__(self, name, maxHP)
        self.abilites = {
            "attack" : 3,
            "defence" : 6,
            "speed" : 6
        }