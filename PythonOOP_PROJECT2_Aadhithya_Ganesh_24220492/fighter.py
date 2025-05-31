from creature import Creature
from termcolor import colored

class Fighter(Creature):
    # Constructor to initialize the stats for the Fighter. 
    # We can set the name, hp and maxHP by calling the super class constructor of creature.
    def __init__(self, name, maxHP = 50):
        Creature.__init__(self, name, maxHP)
        self.abilites = {
            "attack" : 5,
            "defence" : 8,
            "speed" : 5
        }
    
    # Selects the target with the most HP
    def auto_select(self, target_list):
        if len(target_list) == 0 or max(target_list).hp == 0:
            return None
        target = max(target_list)
        return target
        
    # Method to auto select a target from the list of targets and attack that target.
    # There is an attack strategy for Fighter. 
    # The Fighter makes a total of 3 attacks each turn. 
    # The last 2 are made with a -3 penalty on the attack ability. 
    # As long as the target isn’t defeated it remains the target of the second or third attack. 
    # If it gets defeated though before the Fighter finishes all attacks,select the next target with the most HP.
    def turn(self, round_num, target_list):
        faintedEnemies = []

        target = self.auto_select(target_list)
        
        if not target:
            return "No enemies"

        print(colored(f"{self.name}'s unleashes a flurry of strikes", "light_yellow"))
        for i in range(3):
            if i == 1:
                self.abilites["attack"]-=3
            self.attack(target)
        
            if target.hp == 0:
                faintedEnemies.append(target)
                target = self.auto_select(target_list)

            if not target:
                self.abilites["attack"]+=3
                return faintedEnemies
            
        self.abilites["attack"]+=3
        if len(faintedEnemies) != 0:
            return faintedEnemies
            
