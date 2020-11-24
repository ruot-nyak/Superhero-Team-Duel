from ability import Ability
from armor import Armor
from weapon import Weapon
import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    # def fight(self, opponent):
    #     heroes = [self.name, opponent.name]
    #     winner = random.choice(heroes)
    #     print(f'{winner} won!')
    def add_ability(self, ability):
        # We use the append method to add ability objects to our list.
        self.abilities.append(ability)
    def attack(self):
        """
        calulates the total damage of all ability attacks
        """
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    def add_armor(self, armor):
        """
        adds armor to the armor list
        """
        self.armors.append(armor)
    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        self.current_health -= damage
    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        # TODO: Check the current_health of the hero.
        # if it is <= 0, then return False. Otherwise, they still have health
        # and are therefore alive, so return True
        if self.current_health <= (int(0)):
            return False
        else:
            return True
    def fight(self, opponent):  
        ''' Current Hero will take turns fighting the opponent hero passed in.
        '''
        # TODO: Fight each hero until a victor emerges.
        # Phases to implement:
        # 0) check if at least one hero has abilities. If no hero has abilities, print "Draw"
        # 1) else, start the fighting loop until a hero has won
        # 2) the hero (self) and their opponent must attack each other and each must take damage from the other's attack
        # 3) After each attack, check if either the hero (self) or the opponent is alive
        # 4) if one of them has died, print "HeroName won!" replacing HeroName with the name of the hero, and end the fight loop
        if not self.abilities or not opponent.abilities:
            print('Draw')
        else:
            while True:
                opponent.take_damage(self.attack())
                if opponent.is_alive():
                    pass
                else:
                    print(f'{self.name} wins!')
                    self.add_kill(1)
                    opponent.add_death(1)
                    break

                self.take_damage(opponent.attack())
                if self.is_alive():
                    pass
                else:
                    print(f'{opponent.name} wins!')
                    opponent.add_kill(1)
                    self.add_death(1)
                    break

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths
    
        

# if __name__ == "__main__":
#     # If you run this file from the terminal
#     # this block is executed.
#     hero1 = Hero("Wonder Woman")
#     hero2 = Hero("Dumbledore")

#     hero1.fight(hero2)






if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    ability = Ability("Great Debugging", 50)
    ability2 = Ability('UnGreat Debugging', 25)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    print(hero.abilities)
