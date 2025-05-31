from creature import Creature
import random
from termcolor import colored

class Orc(Creature):
    # Constructor to initialize the stats for the Orc. 
    # We can set the name, hp and maxHP by calling the super class constructor of creature. 
    # Also initialize a isEnraged instance variable
    def __init__(self, name, maxHP = 50):
        Creature.__init__(self, name, maxHP)
        self.abilites = {
            "attack" : 5,
            "defence" : 8,
            "speed" : 3
        }
        self.isEnraged = False

    # Method to perform a heavy attack. Change the stats and make the orcs state enraged. 
    # Then call the super.attack(target). There is no difference in how the attack is made.
    def heavy_attack(self, target):        
        if self.isEnraged == False:
            print(colored(f"{self.name} is in rage", "light_yellow"))
            self.abilites["attack"]+=5
            self.abilites["defence"]-=3
            self.isEnraged = True

        return super().attack(target)

    # Method to perform an attack. If he orc is enraged, change the stat back and make the orcs state not enraged.
    # Then call the super.attack(target). There is no difference in how the attack is made.
    def attack(self, target):
        if self.isEnraged == True:
            print(colored(f"{self.name} cooled down", "light_yellow"))
            self.abilites["attack"]-=5
            self.abilites["defence"]+=3
            self.isEnraged = False
        
        return super().attack(target)

    # Method to auto select a target from the list of targets and attack that target.
    # There is a attack strategy for orc. 
    # Every 4th round the orc gets enraged and does a heavy attack on the target.
    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        
        if not target:
            return "No enemies"

        if round_num % 4 == 0:
            result = self.heavy_attack(target)
            if type(result) != type(None):
                return [result]
        else:
            result = self.attack(target)
            if type(result) != type(None):
                return [result]
