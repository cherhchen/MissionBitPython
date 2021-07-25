usernames = {'IMPerial', 'whiteRabbitCandi', 'cosplayCleric', 'master_eyeball', 'pmer', 'Bedward', 'Lirenlock', 'StabbyStorm', 'Omanyaa', 'eliceh34rt'}
new_user = input("Enter a new username to add to the set of usernames: " + str(usernames) + "\n")

while (new_user in usernames) == True:
    new_user = input("Enter a new username to add to the set of usernames: " + str(usernames) + "\n")
    print("hi") #doesnt print 
else:
    usernames.add(new_user)
    print("Your username was accepted!")
    print(usernames)

