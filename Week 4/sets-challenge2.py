""" Set Challenge

Part 1 - Add a new username
Create a set of usernames
Ask the user for a new username to add to the set of usernames
If the user enters a valid username, add it to the set
Print some message letting the user know the new username was accepted or not
Hint: You'll need some way to tell if the set has changed


Part 2 - Delete an existing username
Ask the user for a username to delete from the set
If the user enters a valis username, delete it from the set
Hint: You can use errors to your advantage


*** Remember, we've come to a point where there can be more than one way to solve the problem. You might end up finding a way to solve these in a way that doesn't use the hints!


BONUS
Change these so that the user is continuously asks for a new username if the entered value was invalid!
"""

usernames = {'IMPerial', 'whiteRabbitCandi', 'cosplayCleric', 'master_eyeball', 'pmer', 'Bedward', 'Lirenlock', 'StabbyStorm', 'Omanyaa', 'eliceh34rt'}

username = input('Add a new username: ')

if username in usernames:
    print("Username " + username + " not accepted")
else:
    print("Username " + username + " was accepted")


delete_username = input("Please delete a username from the set")

if delete_username in usernames:
    usernames.remove(delete_username)
    print(delete_username + " has been deleted from the set")
else:
    print(delete_username + " was not deleted")

print(usernames)
