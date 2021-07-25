"""
Try Except Challenge

Time to break some code! Look up what these differen error types are and find a way to make them happen. Then use Try, Except, and Finally statements to get past them to the next code block. 

BONUS CHALLENGE:
- Try to come up with more than one scenario to break for each one! Some could even be done with user input too.
- Try to cause an "OverflowError" to happen. You'll have to look up what this is and how to break it!
"""

# ZeroDivisionError - when you divide by zero
dividend = int(input("Give a number for the dividend.\n"))
divisor = int(input("Give a number for the divisor. \n"))

try:
    print(dividend/divisor)
except ZeroDivisionError:
    print("We cannot divide by zero.")

# TypeError - when there's a type mismatch (you've seen this before!)
number = int(input("Give me a number. \n"))
word = input("Give me a word. \n")

try:
    print(number + word)
except TypeError:
    print("You have a type error.")


# NameError - when you try to use a variable that doesn't exist yet
try: 
    print(undefined_variable)
except NameError:
    print("You have a name error.")

# ValueError
letter = input("Give me a letter.")
try:
    int(letter)
except ValueError:
    print("You have a value error.")