# Black-Owned Restaurant Finder: Lists exercises

####################################################################################################
# Think about different cuisines (as many as you want) and store them in a list. Using what you
# learned in the previous exercises, write code that asks the user what cuisine they are interested
# in. If the cuisine they entered is not in the list, print the string "Please choose one of these
# cuisines: [LIST OF CUISINES HERE]".

# YOUR CODE HERE
cuisines = ["Chinese", "Japanese", "Korean", "Mediterranean", "Italian", "Indian", "Mexican", "Filipino", "American", "Carribean"]
interest = input("What cuisine are you interested in? \n")

not_cuisine = True
for item in cuisines:
    if item == interest:
        print("Nice! Good choice, I also like " + str(interest) + " too!")
        not_cuisine = False

if not_cuisine == True:    
    print("Please choose one of these cuisines: " + str(cuisines))

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
numberedlist = []
num = 1
for item in black_owned_restaurants:
    numberedlist.append(str(num) + ". " + item)
    print(str(num) + ". " + item)
    num += 1

"""
HARDCODED - does not change if list changes
for i in range(3):
    print(str(i + 1) + ". " + black_owned_restaurants[i])
"""

####################################################################################################
# Find out how far away each restaurant is (in miles) and store those distances in another list.
# Then, print out the name of each restaurant AND how far away it is in a numbered list. Example:
# 1. <RESTAURANT 1> is 2.4 miles away
# 2. <RESTAURANT 2> is 6.8 miles away
# 3. <RESTAURANT 3> is 10.2 miles away

# YOUR CODE HERE
distance = [2.4, 6.8, 10.2]
index = 0
for item in numberedlist:
    print(item + " is " + str(distance[index]) + " away.")
    index += 1

"""
DYNAMIC - changes if list changes
for i in range(len(black_owned_restaurants)):
    print(str(i + 1) + ". " + black_owned_restaurants[i] + " is " + str(distance[i]) + " miles away.")
"""

"""
BONUS CHALLENGE
Repeat the last exercise using a zip
Zip the two lists together
Figure out how to access the items in the zipped list
"""
combined = list(zip(black_owned_restaurants, distance))
print(combined)

#Prints 2.4
print(combined[0][1])

# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week3/black_owned_restaurants_lists.py