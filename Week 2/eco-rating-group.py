""" Room 1 with Cheryl, Angelo, Dina, Emily, Kimberly, and Sammy

Pretend you're working with local families to make their homes more eco-friendly.
Make a variable for a family and give them an eco rating between 1 - 10. Then, print out how eco-friendly that family is.

ex: a house rating at 10 might say "Wow, your house is as eco-friendly as can be!", a house rating below 3 would say something like "There's a bit more you could do to raise your rating". Include two more phrases for ratings 4 - 6 and 7 - 9. (HINT: lots of if and elif!)

Once you get it to work for one house, try changing the house's rating and see how it changes what get's printed!

Bonus:
- if the house rating is low, print out a couple ways the house could increase their rating
- Make a variable that states whether the house made improvements since your last rating. If this is True, raise their rating (use a ternary operator from slide 5!)
"""

johnson_house_eco_rating = int(input("What is the Johnson family eco house rating?"))
print("The Johnson eco-friendly rating is" + str(johnson_house_eco_rating) + " out of 10." )

past_johnson_house_eco_rating = input("What was the Johnson family's previous eco rating?")

improved = True if int(past_johnson_house_eco_rating) < int(johnson_house_eco_rating) else False
""""
if past_johnson_house_eco_rating < johnson_house_eco_rating:
  improved = True
else:
  improved = False
"""
if improved == True:
  johnson_house_eco_rating += 1


if johnson_house_eco_rating <= 4:
  print("The Johnson family eco-house rating is poor. Do better please! \n")
  print("Maybe switch to solar panels...")
elif johnson_house_eco_rating <= 7:
  print("You are doing good!")
  print("Try using reusable paper towels.")
elif johnson_house_eco_rating <= 9:
  print("Wow! You have almost achieved a perfect rating!")
  print("Maybe try using DIY furniture?")
elif johnson_house_eco_rating >= 10:
  print("Spectacular performance! You have achieved a perfect rating! Congratulations for being one of the best at being eco friendly!")

# Determine what level the rating is
# HINT: Look through slides 5 and 7! 

# CODE HERE



# RUN CODE BY NAVIGATING TO THIS DIRECTORY AND TYPING THIS IN THE CONSOLE:  
# python3 eco_friendly_ratings.py
