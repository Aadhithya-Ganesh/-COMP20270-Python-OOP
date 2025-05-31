import random
from termcolor import colored

class Creature:
    # Constructor to initialize the name, hp, maxHP, and the stats of the creature
    def __init__(self, name, maxHP = 10):
        self.name = name
        self.hp = maxHP
        self.maxHP = maxHP
        self.abilites = {
            "attack" : 1,
            "defence" : 5,
            "speed" : 5
        } 
    
    # Method to check if hp < 0. If yes, Make it 0 and return "fainted" 
    def check_life(self):
        if self.hp <= 0:
            self.hp = 0
            return "fainted"
        
    # Method to attack a given target.
    # Get a random number 1 to 20. if targets speed + defence <= the random number, The target will get hit.
    # Damage will be targets attack + a random number from 1 to 4
    def attack(self, target):
        print(colored(self.name, "light_blue"), "Attacks", colored(target.name, "light_red"))
        roll = random.randint(1,20)

        if target.abilites["speed"] + target.abilites["defence"] <= roll:
            damage = self.abilites["attack"] + random.randint(1,4)
            target.hp-=damage
            print(colored(f"{self.name} hits for {damage} damage!", "light_green"))
            if target.check_life() == "fainted":
                print(colored(f"{target.name} Fainted", "light_green"))
                return target
            else:
                print(colored(f"Remaining hp : {str(target.hp)} / {str(target.maxHP)}", "yellow"))

        else:
            print(colored("Attack missed", "red"))


    # Select a random target from the list of targets.
    def auto_select(self, target_list):
        if len(target_list) == 0:
            return None
        target = random.choice(target_list)
        return target

    # Method to auto select a target from the list of targets and attack that target
    # There is no attack strategy.
    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        
        if not target:
            return "No enemies"
    
        result = self.attack(target)
        if type(result) != type(None):
            return [result]

    def __eq__(self, other):
        if self.name == other.name:
            return True
        else:
            return False
        
    def __str__(self):
        return self.name + " : " + str(self.hp)
    
    def __repr__(self):
        return self.name + " : " + str(self.hp)
    
    def __lt__(self, other):
        return self.hp < other.hp
    