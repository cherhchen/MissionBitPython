# Example of VARIABLES

# You have a pet rescue and you want people to know what each Dog is like!
# You create a way to assign playfulness, affection, and shedding level to each different dog
# so prospective parents can view their qualities!


class Dog:
    playfulness = 0
    affection = 0
    shedding = 0

    def __init__(self, playfulness, affection, shedding):
        self.playfulness = playfulness
        self.affection = affection
        self.shedding = shedding

    def dog_bio(self):
      bio = "Playfulness: " + str(self.playfulness) + "\nAffection: " + str(self.affection) + "\nShedding: " + str(self.shedding)
      # TODO
      # 1. Reassign bio to be a string that describes the dog
      # HINT: we haven't learned about classes yet, but you can look at lines 14-16 to see how to get those variables!
      # 2. Print out the bio
      return bio


golden_retriever = Dog(10, 10, 10)
print("Golden Retriever Bio \n" + golden_retriever.dog_bio())
pug = Dog(6, 9, 3)
print("Pug Bio \n" + pug.dog_bio())
poodle = Dog(4, 10, 1)
print("Poodle Bio \n" + poodle.dog_bio())
# TODO: add more dogs!

# RUN CODE BY NAVIGATING TO THIS DIRECTORY AND TYPING THIS IN THE CONSOLE: 

# python3 dogs.py

# SUPER CHALLENGE
# **This touches on some things we haven't covered yet!
# See if you can find the pattern when it comes to the assignments
# Try to add a variable called "name"