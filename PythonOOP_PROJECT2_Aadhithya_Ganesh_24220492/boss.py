from orc import Orc
import random
from termcolor import colored

class Boss(Orc):
    # Constructor to initialize the stats for the Boss. 
    # We can set the name, hp and maxHP by calling the super class constructor of Orc.
    def __init__(self, name, maxHP = 200):
        Orc.__init__(self, name, maxHP)
        self.abilites = {
            "attack" : 5,
            "defence" : 8,
            "speed" : 5
        }
    
    # The Boss battle strategy is a mix between the Orc and the Fighter. 
    # In round 1 it makes three attacks just like the Fighter but the first target is selected using the ’Weak’ mode and if it fells its
    # target the rest use the ’Random’ mode. For turns 2,3,4 it uses heavy attack using the ’Strong’ mode
    def auto_select(self, target_list, mode):
        if len(target_list) == 0:
                return None
        
        if mode == "weak":
            return min(target_list)

        elif mode == "strong":
            return max(target_list)
        else:
            target_list = list(filter(lambda item : item != max(target_list) or item != min(target_list), target_list))
            if len(target_list) == 0:
                return None
            return random.choice(target_list)

    # Method to auto select a target from the list of targets and attack that target.
    # It choses a target based on 3 different modes. 
    # ’Strong’ is for the strongest in the list 
    # ’Weak’ for the weakest in the list
    # ’Random’ for randomly between strongest and weakest. 
    # Weakest and strongest is defined by HP.
    def turn(self, round_num, target_list): 
        if round_num % 4 == 1:
            faintedEnemies = []

            target = self.auto_select(target_list, "weak")

            print(colored(f"{self.name}'s unleashes a flurry of strikes", "light_yellow"))
            for i in range(3):
                if i == 1:
                    self.abilites["attack"]-=3
                self.attack(target)
            
                if target.hp == 0:
                    faintedEnemies.append(target)
                    target = self.auto_select(target_list, "random")

                if not target:
                    self.abilites["attack"]+=3
                    return faintedEnemies
            
            self.abilites["attack"]+=3
            if len(faintedEnemies) != 0:
                return faintedEnemies
        else:
            target = self.auto_select(target_list, "strong")

            result = self.heavy_attack(target)
            if type(result) != type(None):
                return [result]      

    def __lt__(self, other):
        return self.hp < other.hp
