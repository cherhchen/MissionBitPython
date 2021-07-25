# Example of LISTS

# You want to set up a linkedin account to have a record of all of your experiences and education

# You set up your account and list these items as your experiences and education when it asks you
# for information
my_experiences = ["Waiter", "Coder"]
my_education = ["High School"]

# You go to college and want to update your Linkedin!

# Luckily you can go back and append to your list of experiences and education. Add one new experience (ex: "Teaching assistant") and one new education (ex: "College")
my_experiences.append("Teaching assistant")
my_education.append("College")

# Now print the list out so you will get Waiter, Coder AND the new experience you entered above
print(my_experiences)

# Now print the list so you will get High School AND the new education you entered
print(my_education)

"""
BONUS
1. Make an empty list
2. Add to that list the number of months you were doing each experience.
3. Zip the two lists together
4. Print it out!
"""

months = []
months.append("1 month")
months.append("2 months")
months.append("3 months")
combined = zip(my_experiences, months)
print(list(combined))



# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 week3/linkedIn.py