""" 
Pretend you're working with local families to make their homes more eco-friendly.
Make a variable for a family and give them an eco rating between 1 - 10. Then, print out how eco-friendly that family is.
ex: a house rating at 10 might say "Wow, your house is as eco-friendly as can be!", a house rating below 3 would say something like "There's a bit more you could do to raise your rating". Include two more phrases for ratings 4 - 6 and 7 - 9.

Once you get it to work for one house, try changing the house's rating and see how it changes what get's printed!

Bonus:
- if the house rating is low, print out a couple ways the house could increase their rating
- Make a variable that states whether the house made improvements since your last rating. If this is True, raise their rating
"""

# Variable for house and it's rating
rating = 3
previousrating = input("What was your previous house rating? \n")

if rating > int(previousrating):
    improved = True
else:
    improved = False

if improved == True:
    rating += 1
# CODE HERE

# Determine what level the rating is
# HINT: Look through slides 5 and 7! 

# CODE HERE
if rating <= 3:
    print("Yikes! Your house needs significant work to raise your eco-friendly rating.")
    print("""
    Things You Can Do To Raise Your Rating:
    DIY instead of buying new
    Swap regular light bulbs for LED bulbs
    Recycle and compost
    Decorate your house with plants
    Install solar panels
    """)
elif rating <= 6:
    print("Eh...you can do better to raise your eco-friendly rating.")
    print("""
    Ever Considered:
    Using homemade natural cleaning products
    Using more rags, fewer paper towels
    Line-drying when possible
    Using cold water when washing your clothes
    Upgrading to a smart thermostat
    Cleaning your fridge coils
    """)
elif rating <= 9:
    print("Alright alright, not too shabby, mate! Your house is pretty eco-friendly.")
else:
    print("Wow! Your house is as eco-friendlly as can be! Gold star for you!")


# RUN CODE BY NAVIGATING TO THIS DIRECTORY AND TYPING THIS IN THE CONSOLE:  
# python3 eco_friendly_ratings.py
