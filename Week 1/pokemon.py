# Example of VARIABLES


# You want to make a Pokemon game, and want people to have a way to choose which Pokemon they would
# prefer
# You create a way to assign attack, defense, speed and hp
class Pokemon:
    attack = 0
    defense = 0
    speed = 0
    hp = 0

    def __init__(self, attack, defense, speed, hp):
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.hp = hp

    def pokemon_bio(self):
      bio = " attack level is " + str(self.attack) + ", defense level is " + str(self.defense) + ", speed level is " + str(self.speed) + ", and hp level is " + str(self.hp) + "."
      # TODO
      # 1. Reassign bio to be a string that describes the pokemon
      # HINT: we haven't learned about classes yet, but you can look at lines 14-16 to see how to get those variables!
      # 2. Print out the bio
      return bio


pikachu = Pokemon(55, 40, 90, 35)
print("Pikachu's" + pikachu.pokemon_bio())
bulbasaur = Pokemon(49, 49, 45, 45)
print("Bulbasaur's" + bulbasaur.pokemon_bio())
charmander = Pokemon(52, 43, 65, 39)
print("Charmander's" + charmander.pokemon_bio())
# TODO: add more Pokemon!


# RUN CODE BY NAVIGATING TO THIS DIRECTORY AND TYPING THIS IN THE CONSOLE: 

# python3 pokemon.py

# SUPER CHALLENGE
# **This touches on some things we haven't covered yet!
# See if you can find the pattern when it comes to the assignments
# Try to add a new variable called "rarity"