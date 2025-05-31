from goblinking import GoblinKing
from orcgeneral import OrcGeneral
from goblin import Goblin
from orc import Orc
from fighter import Fighter
from archer import Archer
from warrior import Warrior
from creature import Creature
from boss import Boss
from wizard import Wizard
import time
from termcolor import colored

class Battle():
    # Constructor to define the battle environment
    # Initialize the enemies, allies, boss, and wizard.
    def __init__(self):
        self.enemies = [Orc("Thrall"), OrcGeneral("Saurfang"), Goblin("Gollum"), GoblinKing("Goblin King")]
        self.allies = [Fighter("Aragorn"), Archer("Legolas"), Creature("Frodo"), Warrior("Boromir")]

        self.boss = [Boss("Arthas")]
        self.wizard = [Wizard("Gandalf")]


    # Defines the order in which each creature should attack
    def order(self):
        creatures = self.enemies + self.allies + self.wizard

        creatures.sort(key = lambda item : item.abilites["speed"], reverse=True)
        
        return creatures
    
    # Check if the boss can enter the battle
    # If the avg hp of the enemeies is < 40%, the boss enters.
    def canBossEnter(self):
        hp = sum(list(map(lambda item : item.hp, self.enemies)))
        maxHP = sum(list(map(lambda item : item.maxHP, self.enemies)))
        if hp / 195 < 0.4:
            print(self.boss[0].name, "enters the battle")
            return True
        else:
            return False
        

    # Starts the battle
    # The battle ends with the allies, or wizard or enemies die
    # You can quit the game by typing quit on the wizards turn.
    def start(self):
        quit = None
        round = 1
        while True:
            if self.boss[0] not in self.enemies and self.canBossEnter() and len(self.enemies) != 0:
                self.enemies+=self.boss
            creatures = self.order()
            print(creatures)
            print(colored(f"Round {round} :", "magenta"))
            for creature in creatures:
                if creature.hp == 0:
                    continue

                if creature in self.allies:
                    target_list = self.enemies
                else:
                    target_list = self.allies + self.wizard
                
                if type(creature) == type(Wizard("")):
                    result = creature.turn(self.allies + self.wizard, self.enemies)
                else:
                    result = creature.turn(round, target_list)

                print()

                if type(result) != type(None) and type(result) != type("str"):
                    if creature in self.allies or creature in self.wizard:
                        self.enemies = list(filter(lambda item : item not in result, self.enemies))
                    else:
                        self.allies = list(filter(lambda item : item not in result, self.allies))
                        self.wizard = list(filter(lambda item : item not in result, self.wizard))
                elif result == "quit":
                    print(colored("Quiting...", "light_yellow"))
                    quit = True
                    break

                if len(self.wizard) == 0:
                    print(colored("Player is dead!", "light_red"))
                    quit = True
                    break
                elif len(self.allies) + len(self.wizard) == 0:
                    print(colored("All allies dead. Enemies won", "light_red"))
                    quit = True
                    break
                elif len(self.enemies) == 0:
                    print(colored("All enemies dead. Allies won", "light_green"))
                    quit = True
                    break
                
                time.sleep(1)

            if quit == True:
                break

            print()
            round+=1


        print(" ____________                            _______        _______                     _______   ______ ")
        print("|                   |       |        |  |              |       |   |            |  |         |      |")
        print("|                  | |      | |    | |  |              |       |    |          |   |         |      |")
        print("|                 |   |     |  |  |  |  |              |       |     |        |    |         |______|")
        print("|      _____     |_____|    |   ||   |  |____          |       |      |      |     |___      |    |")
        print("|     |     |   |       |   |        |  |              |       |       |    |      |         |     |")
        print("|     |     |  |         |  |        |  |              |       |        |  |       |         |      |")
        print("|_____|     | |           | |        |  |________      |_______|         |         |________ |       |")
        print("\n\n")