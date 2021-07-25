# Black-Owned Restaurant Finder: Lists exercises

####################################################################################################
# Think about different cuisines (as many as you want) and store them in a list. Using what you
# learned in the previous exercises, write code that asks the user what cuisine they are interested
# in. If the cuisine they entered is not in the list, print the string "Please choose one of these
# cuisines: [LIST OF CUISINES HERE]".

# YOUR CODE HERE
cuisines = ["Chinese", "Japanese", "Korean", "Mediterranean", "Italian", "Indian", "Mexican", "Filipino", "American", "Carribean"]
interest = input("What cuisine are you interested in? \n")

if interest not in cuisines:
    print("Please choose one of these cuisines: " + str(cuisines))

"""
if interest == "Chinese" or  interest == "Japanese" or  interest == "Korean" or interest == "Mediterranean" or  interest == "Italian" or  interest == "Indian" or  interest == "Mexican" or interest == "Filipino" or interest == "American" or interest == "Carribean":
    print("Nice! Good choice, I also like " + str(interest) + " too!")
else:
    print("Please choose one of these cuisines: " + str(cuisines))
"""

####################################################################################################
# Find the name of at least three black-owned restaurants nearby and store their names in a list.
# Then, print out the name of each restaurant, one line at a time.

# TIP: Use Google Maps to find nearby black-owned restaurants
# https://www.google.com/maps/search/black+owned+restaurants

# YOUR CODE HERE
black_owned_restaurants = ["Tastebuds", "Little Skillet", "Voodoo Love Restuarant"]

####################################################################################################
# Take your list of restaurants from the previous challenge and print them out in a numbered list.
# Example:
# 1. <RESTAURANT 1>
# 2. <RESTAURANT 2>
# 3. <RESTAURANT 3>

# YOUR CODE HERE
numbers = ["1. ", "2. ", "3. "]

####################################################################################################
# Find out how far away each restaurant is (in miles) and store those distances in another list.
# Then, print out the name of each restaurant AND how far away it is in a numbered list. Example:
# 1. <RESTAURANT 1> is 2.4 miles away
# 2. <RESTAURANT 2> is 6.8 miles away
# 3. <RESTAURANT 3> is 10.2 miles away

# YOUR CODE HERE
distance = ["is 0.5 miles away", "is 2.5 miles away", "is 5 miles away"]
print(list(zip(numbers, black_owned_restaurants, distance)))

# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week3/black_owned_restaurants_lists.py
