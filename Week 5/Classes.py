class Classes:
    # mascot = "bunnies"
    # learning_code_amount_percent = 65

    def __init__(self, mascot):
        self.mascot = mascot
        print("Yay class start! " + self.mascot)

    def printMascot(self, param):
        m = self.mascot
        print("The class mascot is: " + m)
        print("My favorite animal is: " + param)

    def class_values(self):
        print("Growth, Creativity, and Commitment!")

Bunnies = Classes("Bunnies")
Ornelle = Classes("Cats")
Hunter = Classes("Dogs")

print(type(Bunnies))
# print(mascot) --> out of scope

"""
Bunnies.mascot
Bunnies.printMascot("Bunnies")
Bunnies.printMascot("Cats")
Bunnies.printMascot('')
Bunnies.class_values()
"""

