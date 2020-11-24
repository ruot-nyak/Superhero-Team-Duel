import random


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        found_hero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                found_hero = True
        if not found_hero:
            return 0
    
    def view_all_heroes(self):
        for hero in self.heroes:
            print(f'{hero}')
    
    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
        print("{} Kill/Deaths:{}".format(hero.name,kd))
    
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
               # TODO: Complete the following steps:
            # 1) Randomly select a living hero from each team (hint: look up what random.choice does)
            # 2) have the heroes fight each other (Hint: Use the fight method in the Hero class.)
            # 3) update the list of living_heroes and living_opponents
            # to reflect the result of the fight
            random_hero = random.choice(living_heroes)
            random_opponent = random.choice(living_opponents)
            random_hero.fight(random_opponent)
            if random_hero.is_alive:
                living_opponents.remove(random_opponent)
            else:
                living_heroes.remove(random_hero)