# Lists allow you to store sets of information in one place.
#
# A list is a collection of items in a particular order.

# Use random to generate random numbers
import random

# Creating a list
my_list = ["lewis", "is", "hungry"]
print(my_list)
print(my_list[0])
print(my_list[0].title())

# Accessing the last element in a list
print(my_list[-1])

# Assigning a string to the last element
my_list[-1] = "full"
print(my_list)

# Appending an element to the end of a list
my_list.append('appended')
print(my_list)

# Inserting elements into a list
my_list.insert(0, 'prepended')
print(my_list)

# Deleting an element from a list
del my_list[1]
print(my_list)

# Popping end element from list
popped_off = my_list.pop()
print(popped_off)
print(my_list)

# Pop() to remove an item from any position
a = my_list.pop(2)
print(a)
print(my_list)

# Remove an item by value
my_list.remove('prepended')
print(my_list)

# Generate a list of random numbers
num_list = []
i = 0
while i < 100:
    num_list.append(random.randint(0, 2000))
    i = i + 1

print(num_list)

# Sort list
num_list.sort()
print(num_list)
num_list.sort(reverse=True)
print(num_list)

# To maintain the original order of a list but present it in a sorted order
# you can use the sorted() function, it allows you to display your list in
# a particular order but doesn't mutate the original list
print(sorted(num_list))

# To find the length of a list
len = len(num_list)
print(f'The list has {len} elements')


