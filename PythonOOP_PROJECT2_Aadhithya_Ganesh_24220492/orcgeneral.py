from orc import Orc
from warrior import Warrior

class OrcGeneral(Orc, Warrior):
    # Constructor to initialize the stats for the orc general. 
    # We can set the name, hp, maxHP and abilities by calling the super class constructor of orc.
    def __init__(self, name, maxHP = 80):
        Orc.__init__(self, name, maxHP)

    # Method to auto select a target from the list of targets and attack that target.
    # There is a attack strategy for orc general which follows the strategy of both orc and warrior. 
    # In the 1st round, Orc general attack the target and call shield_up().
    # In the 2nd round, Orc general attack the target.
    # In the 3rd round, Orc general call shield_down() and attack the target.
    # In the 4th round, Orc general becomes enraged and does a heavy attack on the target.
    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        
        if not target:
            return "No enemies"

        if round_num % 4 == 1:
            result = self.attack(target)
            self.shield_up()
            if type(result) != type(None):
                return [result]
        elif round_num % 4 == 2:
            result = self.attack(target)
            if type(result) != type(None):
                return [result]
        elif round_num % 4 == 3:
            self.shield_down()
            result = self.attack(target)
            if type(result) != type(None):
                return [result]
        else:
            result = self.heavy_attack(target)
            if type(result) != type(None):
                return [result]