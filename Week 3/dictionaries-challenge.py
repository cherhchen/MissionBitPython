#----------------------------------------------------------
# Challenge 1: Sum Values
#----------------------------------------------------------

# Create a dictionary called groceries. Print the sum of the values of the dictionary

# Write your code here:
groceries = {"apple": 3, "potato": 4, "asparagus": 9, "kale": 6, "cake": 14}
print("The sum of the values is " + str(sum(groceries.values())))

#----------------------------------------------------------
# Challenge 2: Max Value
#----------------------------------------------------------

# Create a dictionary called groceries with items as the keys and prices as the values. Print the highest price of a grocery.

# Write your code here:
print("The max of the values is " + str(max(groceries.values())))


#----------------------------------------------------------
# Challenge 3: Grouping food
#----------------------------------------------------------

# Create a dictionary called groceries with the name of the grocery as the keys and the food group as the value. Print each food group with the number of items in the food group.

# Write your code here:
groceries2 = {"apple": "fruit", "potato": "starch", "asparagus": "vegetable", "kale": "vegetable", "cake": "sweets"}

fruit_group = 0
starch_group = 0
vegetable_group = 0
sweets_group = 0

for i in groceries2:
    if groceries2[i] == "fruit":
        fruit_group += 1
    elif groceries2[i] == "starch":
        starch_group += 1
    elif groceries2[i] == "vegetable":
        vegetable_group += 1
    elif groceries2[i] == "sweets":
        sweets_group += 1

print(fruit_group, starch_group, vegetable_group, sweets_group)


#----------------------------------------------------------
# Challenge 4: Updating values
#----------------------------------------------------------

# Create a dictionary called groceries with items as the keys and prices as the values. Compute the average price of all of the foods, and update the price of all of the food keys to now be equal to the average price.

# Write your code here:
groceries3 = {"apple": 3, "potato": 4, "asparagus": 9, "kale": 6, "cake": 14}

total_price = 0
for i in groceries3:
    total_price += groceries3[i]

avg_price = total_price / len(groceries3)

for x in groceries3:
    groceries3[x] = avg_price

print(groceries3)


#----------------------------------------------------------
# Challenge 5: List values
#----------------------------------------------------------

# Create a dictionary called groceries with the name of the grocery as the key and a list of the stores it is available at as the value. Print out the store that the most amount of foods are available at.

# Write your code here:
groceries4 = {'apple': ['Safeway', 'Costco', 'Lucky', 'Walmart'], 'orange': ['Costco', 'Walmart'], 'peach': ['Safeway', 'Costco'], 'pear': ['Safeway', 'Costco', 'Lucky']}

safeway = 0
costco = 0
lucky = 0
walmart = 0

index = 0
for key in groceries4:
    for store in groceries4[key]:
        if groceries4[key][index] == 'Safeway':
            safeway += 1
        elif groceries4[key][index] == 'Costco':
            costco += 1
        elif groceries4[key][index] == 'Lucky':
            lucky += 1
        elif groceries4[key][index] == 'Walmart':
            walmart += 1
        index += 1
    index = 0

items_available = {'Safeway': safeway, 'Costco': costco, 'Lucky': lucky, 'Walmart': walmart}

max_number = items_available['Safeway']
max_store = 'Safeway'
for store in items_available:
    if items_available[store] > max_number:
        max_number = items_available[store]
        max_store = store

print(max_store + " has the most amount of food available: " + str(max_number))



#----------------------------------------------------------
# Challenge 6: Even Keys
#----------------------------------------------------------

# Create a dictionary named ints, with all integer keys and values. Print the sum of the values of all even keys.

# Write your code here:
ints = {1:11, 2:12, 3:13, 4:14}

sum_of_even_keys = 0
for i in ints:
    if i % 2 == 0:
        sum_of_even_keys += i

print("The sum of the values of all even keys is " + str(sum_of_even_keys))

#----------------------------------------------------------
# Challenge 7: Add Ten
#----------------------------------------------------------

# Create a dictionary with integer values named integers. Add 10 to every value in my_dictionary and print my_dictionary

# Write your code here:
integers = {5:0, 6:0, 7:0, 8:0}
for i in integers:
    integers[i] = i + 10

print(integers)

#----------------------------------------------------------
# Challenge 8: Largest Value
#----------------------------------------------------------

# Create a dictionary named max_nums with all integer values. Print the key associated with the largest value in the dictionary.

# Write your code here:
max_nums = {'a': 12, 'b': 7, 'c': 54, 'd': 23, 'e': 3}

max_key = 'a'
for num in max_nums:
    if max_nums[num] > max_nums[max_key]:
        max_key = num

print("The max key is " + max_key)
    

#----------------------------------------------------------
# Challenge 9: Word Length Dict
#----------------------------------------------------------

# Create a list of strings named words. Print a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.

# Write your code here:
words_list = ["one", "two", "three", "four", "five"]
words_dict = {}
for a_word in words_list:
    words_dict[a_word] = len(a_word)

print(words_dict)
    
#----------------------------------------------------------
# Challenge 10: Contact Data
#----------------------------------------------------------

#Create a dictionary called contact_data that stores a list of contact data for your friends and family. This dictionary should include name as the key and have phone number, email address and home address in the value. Print out the email of every person in the dictionary.

#Write your code here:
contact_data = {"Bob": ["123-456-7890", "bobbugsbegone@gmail.com", "123 Bug Boulevard"], "Gabe": ["453-436-5580", "yogabbagabba@gmail.com", "345 Angel Lane"], "PJ": ["533-789-3581", "peanutbutterandjelly@gmail.com", "421 Sandwich Avenue"]}
for contact in contact_data:
    print(contact_data[contact][1])
#should print out all email addresses of contacts


# RUN CODE BY TYPING THIS IN THE CONSOLE: 

# python3 dictionaries_challenge.py