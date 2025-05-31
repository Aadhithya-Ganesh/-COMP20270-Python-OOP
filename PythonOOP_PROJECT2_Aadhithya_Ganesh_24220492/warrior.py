from creature import Creature
from termcolor import  colored

class Warrior(Creature):
    # Constructor to initialize the stats for the Warrior. 
    # We can set the name, hp and maxHP by calling the super class constructor of creature. 
    # Also initialize a isShieldUp instance variable
    def __init__(self, name, maxHP = 50):
        Creature.__init__(self, name, maxHP)
        self.abilites = {
            "attack" : 5,
            "defence" : 10,
            "speed" : 4
        }
        self.isShieldUp = False

    # Method to change the stats of the warrior and make isShieldUp to true
    def shield_up(self):
        print(colored(f"{self.name} takes a defensive stance", "light_yellow"))
        self.abilites["attack"]-=4
        self.abilites["defence"]+=4
        self.isShieldUp = True

    # Method to change the stats of the warrior and make isShieldUp to false
    def shield_down(self):
        print(colored(f"{self.name} stance returns to normal.", "light_yellow"))
        self.abilites["attack"]+=4
        self.abilites["defence"]-=4
        self.isShieldUp = False

    # Method to auto select a target from the list of targets and attack that target.
    # There is a attack strategy for warrior. 
    # In the 1st round, warrior attacks the target and calls shield_up()
    # In the 2nd and 3rd round, warrior attacks the target
    # In the 4th round, warrior calls shield_down() and attacks the target and 
    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        
        if not target:
            return "No enemies"

        if round_num % 4 == 1:
            result = self.attack(target)
            self.shield_up()
            if type(result) != type(None):
                return [result]

        elif round_num % 4 == 2 or round_num % 4 == 3:
            result = self.attack(target)
            if type(result) != type(None):
                return [result]
        else:
            self.shield_down()
            result = self.attack(target)
            if type(result) != type(None):
                return [result]


