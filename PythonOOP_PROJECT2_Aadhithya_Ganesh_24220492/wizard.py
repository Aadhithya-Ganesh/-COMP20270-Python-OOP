from creature import Creature
import random
from termcolor import colored

class Wizard(Creature):
    # Constructor to initialize the stats for the Wizard. 
    # We can set the name, hp and maxHP by calling the super class constructor of creature. 
    # Also initialize a mana instance variable to 100
    def __init__(self, name, maxHP = 20):
        Creature.__init__(self, name, maxHP)
        self.abilites = {
            "attack" : 3,
            "defence" : 5,
            "speed" : 5,
            "arcana" : 10
        }
        self.mana = 100

    # Method to perform an attack. Call the super.attack(target). 
    # There is no difference in how the attack is made.
    # The wizard get 20 mana after the attack.
    # All the isManaFull() method to make mana as 100 if mana > 100
    def attack(self, target):
        result = super().attack(target)
        self.mana+= 20
        if self.isManaFull() : print("Mana Full")
        else: print("Mana: +20")
        return result
    
    # Method to check if mana > 100, set the mana to 100 and return True
    def isManaFull(self):
        if self.mana > 100:
            self.mana = 100
            return True
    
    # Method to add 30 Mana to the wizard.
    def recharge(self):
        self.mana+=30
        print(colored(f"Gandalf channels magical energy...", "light_yellow"))
        if self.isManaFull() : print(colored(f"Mana Full", "light_yellow"))
        else: print(colored(f"Mana: +30", "light_yellow"))

    # Method to fire a bolt on the given target. 
    # Select a number from 1 to 20 and add half the arcana value to the roll
    # If the targets speed and defence <= roll, the target will get hit
    # Damage will be a random number from 1 to arcana value
    # The wizard also gets 10 mana.  
    def fire_bolt(self, target):
        print(colored(self.name, "light_blue"), "fires a fire bolt at", colored(target.name, "light_red"))
        roll = random.randint(1,20) + self.abilites["arcana"] // 2

        if target.abilites["speed"] + target.abilites["defence"] <= roll:
            damage = random.randint(1,self.abilites["arcana"])
            target.hp-=damage
            self.mana+=10
            if self.isManaFull() : print(colored("Mana Full", "light_yellow"))
            else: print(colored("Mana: +10", "light_yellow"))
            print(colored(f"Fire bolt hits for {damage} fire damage!", "light_green"))
            if target.check_life() == "fainted":
                print(colored(f"{target.name} Fainted", "light_green"))
                return target
            else:
                print(colored(f"Remaining hp : {str(target.hp)} / {str(target.maxHP)}", "light_yellow"))

        else:
            print(colored("Attack missed", "red"))
    
    # Method to heal a given target. 
    # If wizards mana is < 20, Nothing should happen
    # Heals the target for a random number from 0 to 8 + the half of the wizards arcana value
    # Make sure the targets hp doesnt exceed its maxHP
    def heal(self, target):
        if self.mana < 20:
            print(colored(f"Not enough Mana", "red"))
            return

        self.mana-=20
        print(colored(f"Mana: -20", "light_yellow"))
        heal = random.randint(0,8) + self.abilites["arcana"] // 2
        if target.hp + heal > target.maxHP:
            target.hp = target.maxHP
        else:
            target.hp+=heal

        print(colored(f"{self.name} heals {target.name} for {heal} HP", "light_green"))

    # Method to heal the list of targets
    # If wizards mana is < 30, Nothing should happen
    # Heals the target for a random number from 0 to 10 + the wizards arcana value
    # Make sure the target's hp doesnt exceed its maxHP
    def mass_heal(self, allies):
        if self.mana < 30:
            print(colored(f"Not enough Mana", "red"))
            return
        
        self.mana-=30
        print(colored(f"Mana: -30", "light_yellow"))
        for ally in allies:
            heal = random.randint(0,10) + self.abilites["arcana"]
            print(colored(f"{self.name} heals {ally.name} for {heal} HP", "light_green"))
            if ally.hp + heal > ally.maxHP:
                ally.hp = ally.maxHP
            else:
                ally.hp+=heal

    # Method to damage all the list of targets with fire power
    # If wizards mana is < 30, Nothing should happen
    # Damage is a random number from 5 to 20 + the wizards arcana value
    # Roll is a random number from 1 to 20 + the enemies speed
    # If roll is >= wizards arcana, the target takes half the damage
    # else The target takes full damage
    def fire_storm(self, enemies):
        if self.mana < 50:
            print(colored(f"Not enough Mana", "red"))
            return
        
        self.mana-=50
        print(colored(f"Mana: -50", "light_yellow"))
        for enemy in enemies:
            damage = random.randint(5, 20) + self.abilites["arcana"]
            roll = random.randint(1, 20) + enemy.abilites["speed"]
            if roll >= self.abilites["arcana"]:
                print(colored(f"Fire Storm deals {damage // 2} fire damage to {enemy.name}", "light_green"))
                enemy.hp-=damage // 2
            else:
                print(colored(f"Fire Storm deals {damage} fire damage to {enemy.name}", "light_green"))
                enemy.hp-=damage

            if enemy.check_life() == "fainted":
                print(colored(f"{enemy.name} Fainted", "light_green"))
            else:
                print(colored(f"Remaining hp : {str(enemy.hp)} / {str(enemy.maxHP)}", "light_yellow"))

        return list(filter(lambda item : item.hp == 0, enemies))

    # Method to ask the user to select a target from the list of target_list until a correct on is entered.
    # Returns the chosen target back.
    def select_target(self, target_list):
        print("Select target:")
        while True:
            for i in range(len(target_list)):
                print(str(i + 1) + ": " + target_list[i].name + ", HP: " + str(target_list[i].hp) + "/" + str(target_list[i].maxHP))
            choice = int(input("Enter choice : "))
            if choice < 1 and choice > len(target_list):
                print("Enter a valid choice")
            else:
                break
        return target_list[choice - 1]
        
    # Method to ask the user for an action to be performed by the wizard.
    # There are several actions 
    # Action F: Attack : Takes a target to attack
    # Action R: Recharge : Calls the recharge method
    # Action 1: Heal : Takes a target to heal
    # Action 2: Firebolt : Takes a target to firebolt
    # Action 3: Mass heal: Calls the mass heal method on the list of allies
    # Action 4: Firestorm: Calls the firestorm method on the list of enemies
    # Action Quit: Quits the game 
    def turn(self, allies, enemies):
        print("========================================================")
        print(colored(f"Player: {self.name}", "light_magenta"), colored(f", HP: {self.hp} / {self.maxHP}", "light_green"), colored(f", Mana: {self.mana} / 100", "light_blue"))
        print("========================================================")
        print(colored("Allies", "light_green"))
        for ally in allies:
            print(ally.name + ", HP: " + str(ally.hp) + "/" + str(ally.maxHP))
        print("========================================================")
        print(colored("Enemies", "light_red"))
        for enemy in enemies:
            print(enemy.name + ", HP: " + str(enemy.hp) + "/" + str(enemy.maxHP))
        while True:
            print("========================================================")
            print(f"Actions. F: Attack (+20) R: Recharge Mana (+30)")
            print("Spells. 1: Heal (-20) 2: Firebolt (+10) 3: Mass Heal (-30) 4: Fire Storm (-50)")
            print("To Quit game type: Quit")
            print("========================================================")
            action = input("Enter action : ")
            if action.upper() == "F" or action == "2":
                target = self.select_target(enemies)
                if action.upper() == "F":
                    result = self.attack(target)
                    if type(result) != type(None):
                        return [result]
                else:
                    result = self.fire_bolt(target)
                    if type(result) != type(None):
                        return [result]
                break
            elif action.upper() == "R":
                return self.recharge()
            elif action == "1":
                target = self.select_target(allies)
                return self.heal(target)
            elif action == "3":
                return self.mass_heal(allies)
            elif action == "4":
                return self.fire_storm(enemies)
            elif action.lower() == "quit":
                return action
            else:
                print("Enter a valid action")