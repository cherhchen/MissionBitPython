# Things you need to know:
# Range, Lists, Loops, If statements, Slices, Index/Indices, etc
# ----------------------------------------------------------
# Challenge 1 - Divisible by Ten
# ----------------------------------------------------------
# Make a list within the range 0 to 100. Use a loop to go through
# the list to check if the number is divisible by 10.
# If it is, print out "xx is divisible by 10". Then, print
# out how many were actually divisible by 10.
# ex: [20, 25, 30, 35, 40] would print 3 at the end

# YOUR CODE HERE
numbers = list(range(101))
num_of_divisible = 0

for i in numbers:
    if i % 10 == 0:
        print(str(i) + " is divisible by 10.")
        num_of_divisible += 1
print(str(num_of_divisible) + " numbers were divisible by 10.")

# ----------------------------------------------------------
# Challenge 2 - Greetings
# ----------------------------------------------------------
# Make a list of names. Go through the list and replace each
# name with the word "Hello, " in front of the name.
# (E.g. "Connie" would be replaced with "Hello, Connie") Then print
# the modified list

# YOUR CODE HERE
names = ['Samuel', 'Carla', 'Nadia', 'Guzman', 'Ander', 'Omar', 'Lucrecia', 'Polo']

index = 0
for name in names:
    names[index] = "Hello, " + name
    index += 1
print(names)

"""
for i in range(len(names)):
    print("hello, " + names[i])
"""

# ----------------------------------------------------------
# Challenge 3 - Skip Starting Even Numbers
# ----------------------------------------------------------

# Make a list of integers, then find the first odd element
# and print the rest of the list starting with that numbers
# ex: [4, 8, 10, 11, 12, 15] would print [11, 12, 15].
# Once you print the list, end the loop.
# If every item is even, don't print anything

# YOUR CODE HERE
integers = list(range(10))
for i in integers:
    if i % 2 == 0:
        integers.remove(i)
print(integers)

# ----------------------------------------------------------
# Challenge 4 - Odd Indices
# ----------------------------------------------------------

# Make two lists, one of them with some random numbers of
# your choosing, the other empty. Go through the first list and
# for every index that's odd (1, 3, 5, ...), append that value to the empty list. Then print out the second list.
# (e.g. [4, 3, 7, 10, 11, -2] would print the list [3, 10, -2])

# YOUR CODE HERE
random_list = [0, 2, 7, 13, 24]
empty_list = []

for i in random_list:
    if i % 2 != 0:
        empty_list.append(i)
print(empty_list)

# ----------------------------------------------------------
# Challenge 5 - Exponents
# ----------------------------------------------------------

# Create two lists, one named base and one named power.
# Make a third list that contains every number in base raised
# to every number in power. Then print the list.
# ex: ([2, 3, 4], [1, 2, 3]) would print
# [2, 4, 8, 3, 9, 27, 4, 16, 64]

# YOUR CODE HERE
base = [2, 3, 4]
power = [1, 2, 3]
exponent = []

for b in base:
    for p in power:
        exponent.append(b**p)
print(exponent)

# ----------------------------------------------------------
# Challenge 6 - Larger Sum
# ----------------------------------------------------------

#  Make two lists of integers. Print the list whose elements
# sum to the greater number. If the sum of the elements of
# each lists are equal, print the first list.
# ex: ([1, 9, 5], [2, 3, 7])) would print [1, 9, 5])

# YOUR CODE HERE
list1 = [1, 9, 5]
list2 = [2, 3, 7]

sum1 = 0
sum2 = 0
for i in list1:
    sum1 = sum1 + i

for a in list2:
    sum2 = sum2 + a

if sum1 >= sum2:
    print(list1)
else:
    print(list2)


# ----------------------------------------------------------
# Challenge 7 - Over 9000
# ----------------------------------------------------------

# Loop through a list of integers and sum the elements of the
# list until the sum is greater than 9000. When this happens,
# print the sum and end the loop. If the sum of all of the
# elements is not greater than 9000, then return the
# sum of all the elements. If the list is empty, print 0.
# ex: [8000, 900, 120, 5000] would print 9020

# YOUR CODE HERE
my_list = [8000, 900, 120, 5000]

if len(my_list) == 0:
    print(0)

sum = 0
my_index = 0
while sum < 9000:
    sum = sum + my_list[my_index]
    my_index += 1
else:
    print(sum)   

# ----------------------------------------------------------
# Challenge 8 - Max Num
# ----------------------------------------------------------

# Make a list of your choosing then print out the largest number
# in the list. Print 0 if it's an empty list
# ex: [5, 1, -10, 3, 10, 3, 1, 5, 3] should print 10

# YOUR CODE HERE
num_list = [5, 1, -10, 3, 10, 3, 1, 5, 3]

if len(num_list) == 0:
    print(0)
else:
    num_list.sort()
    print("The largest element is " + str(num_list[len(num_list)-1]))

"""
(1)
max = num_list[0]
for i in num_list:
    if i > max:
        max = i
print(max)
"""

"""
(2)
print(max(num_list))
"""


# ----------------------------------------------------------
# Challenge 9 - Same Values
# ----------------------------------------------------------

# Make two lists of the same length. Print out a list of indices
# where the values were equal for both lists.
# ex: ([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]) would print
# [0, 2, 3]

# YOUR CODE HERE
my_list1 = [5, 1, -10, 3, 3]
my_list2 = [5, 10, -10, 3, 5]
common_values = []

for i in range(len(my_list1)):
    if my_list1[i] == my_list2[i]:
        common_values.append(i)
print(common_values)

# ----------------------------------------------------------
# BONUS Challenge 10 - Reversed List
# ----------------------------------------------------------

# Make two lists of the same length. Print True if lst1 is the
# same as lst2 reversed. Otherwise print False.
# ex: ([1, 2, 3], [3, 2, 1]) should print True, and
# ([1, 5, 3], [3, 2, 1])) should print False

# YOUR CODE HERE
lst1 = [1, 2, 3]
lst2 = [3, 2, 1]

same = True
q = len(lst2) - 1
for p in lst1:
    if p != lst2[q]:
        same = False
        break
    else:
        q -= 1

print(same)



# RUN CODE BY TYPING THIS IN THE CONSOLE:

# python3 loops_challenge.py
