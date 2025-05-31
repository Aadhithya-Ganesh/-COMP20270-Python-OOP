from creature import Creature
import random
from termcolor import colored

class Archer(Creature):
    # Constructor to initialize the stats for the Archer. 
    # We can set the name, hp and maxHP by calling the super class constructor of creature.
    # Also initialize a isEmpowered instance variable
    def __init__(self, name, maxHP = 30):
        Creature.__init__(self, name, maxHP)
        self.abilites = {
            "attack" : 7,
            "defence" : 9,
            "speed" : 8
        }
        self.isEmpowered = False

    # Method to perform a power shot. Change the stats and make the archers state empowered.
    # There is a difference in how the attack is made. 
    # Gets the maximum of 2 random numbers from 1 to 20. If the archers speed is higher than the target, add the difference to the roll
    # if the roll is higher than the targets defence + targets speed, the target is attacked.
    # Damage will be the attack + a random number from 1 to 8
    def power_shot(self, target):
        if self.isEmpowered == False:
            print(colored(f"{self.name}'s attack rises.", "light_yellow"))
            print(colored(f"{self.name}'s defence reduced.", "light_yellow"))
            self.abilites["attack"]+=3
            self.abilites["defence"]-=3
            self.isEmpowered = True
        
        print(colored(self.name, "light_blue"), "shoots", colored(target.name, "light_red"))

        roll = max(random.randint(1,20), random.randint(1,20))

        if self.abilites["speed"] >= target.abilites["speed"]:
            roll+=self.abilites["speed"] - target.abilites["speed"]

        if target.abilites["speed"] + target.abilites["defence"] <= roll:
            damage = self.abilites["attack"] + random.randint(1,8)
            target.hp-=damage
            print(colored(f"Power shot hits for {damage} damage!", "light_green"))
            if target.check_life() == "fainted":
                print(colored(f"{target.name} Fainted", "light_green"))
                return target
            else:
                print(colored(f"Remaining hp : {str(target.hp)} / {str(target.maxHP)}", "light_yellow"))

        else:
            print(colored("Attack missed", "red"))

    # Method to perform an attack. If archer is empowered, Change the stats and make the archers state not empowered. 
    # Then call the super.attack(target). There is no difference in how the attack is made.
    def attack(self, target):
        if self.isEmpowered == True:
            print(colored(f"{self.name}'s abilies return to normal", "light_yellow"))
            self.abilites["attack"]-=3
            self.abilites["defence"]+=3
            self.isEmpowered = False

        return super().attack(target)

    # Select the target with the minimum HP
    def auto_select(self, target_list):
        if len(target_list) == 0:
            return None
        target = min(target_list)
        return target
    
    # Method to auto select a target from the list of targets and attack that target.
    # There is a attack strategy for Archer.
    # In the 1st round, archer attack the target
    # In the 2nd, 3rd and 4th round, the archer power shots the target
    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        
        if not target:
            return "No enemies"

        if round_num % 4 == 1:
            result = self.attack(target)
            if type(result) != type(None):
                return [result]
        else:
            result = self.power_shot(target)
            if type(result) != type(None):
                return [result]


    