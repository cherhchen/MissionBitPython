# ----------------------------------------------------------
# Challenge 1 - Greater than 10
# ----------------------------------------------------------
# Write python that initializes a variable called num to 4 and prints "True" if it is greater than
# 10 and "False" if it is less than 10.  Make sure that is prints out false since num is set to 4.
# Change num to some other values and see what happens!

# Write your code here
num = 4
if num > 10:
    print("True")
else:
    print("False")

# ----------------------------------------------------------
# Challenge 2 - Doubled greater than 10
# ----------------------------------------------------------
# Write python that initializes a variable called num to 4 and prints "True" if 2 times num is
# greater than 10 and "False" if it is less than 10. Make sure that is prints out false since num is
# set to 4. Change num to some other values and see what happens!

# Write your code here
num = 4
if num * 2 > 10:
    print("True")
else:
    print("False")

# ----------------------------------------------------------
# Challenge 3 - Even or Odd
# ----------------------------------------------------------
# Write python that initializes a variable called num to 4 and prints "Odd" if it is odd and "Even"
# if it is even. Make sure that is prints out even since num is set to 4. Change num to some other
# values and see what happens!

# Hint: use mod (%)

# Write your code here
num = 4
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# ----------------------------------------------------------
# Challenge 4 - Favorite Color
# ----------------------------------------------------------
# You want to see if you and your best friend have the same favorite color. Initialize a variable
# called "my_fav_color" and have them initialize one called "friend_fav_color". If they are the
# same, print "We have the same favorite color!" Else, print a message of sadness

# Write your code here
my_fav_color = input("What is your favorite color? \n")
friend_fav_color = input("What is your best friend's favorite color? \n")

if my_fav_color == friend_fav_color:
    print("We have the same favorite color!")
else:
    print("Aw...we do not have the same favorite color :(")

# ----------------------------------------------------------
# Challenge 5 - Favorite Food Type
# ----------------------------------------------------------
# Pick your favorite food from this list: Pizza, Salad, Steak, Strawberries, Ice cream, Cheese,
# Pasta,  Carrots, Apples. Initialize a variable named food to be that food. Then using conditionals
# using the list of food we have, print out what food group the food is from. Your code should still
# work when you change the food variable.

# Hint: use elif

# Write your code here
food = input("Select your favorite food from this list: Pizza, Salad, Steak, Strawberries, Ice cream, Cheese, Pasta, Carrots, Apples \n")

# RUN CODE BY NAVIGATING TO THIS DIRECTORY AND TYPING THIS IN THE CONSOLE: 
if food == "Pizza" or food == "Pasta":
    print("This food item is from the grain group.")
elif food == "Salad" or food == "Carrots":
    print("This food item is from the vegetable group.")
elif food == "Steak":
    print("This food item is from the protein group.")
elif food == "Strawberries" or food == "Apples":
    print("This food item is from the fruit group")
elif food == "Ice cream" or food == "Cheese":
    print("This food item is from the dairy group.")
else:
    print("Please select a food item from the list.") 

# python3 conditionals_mini_challenge.py