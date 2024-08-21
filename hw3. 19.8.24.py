# Example:
# Set
my_set = {1, 2, 3}
print(2 in my_set)  # True

# Dict
my_dict = {'a': 1, 'b': 2}
print(my_dict['a'])  # 1

# Break down:
"""In Python, set and dict (dictionary) share some similarities but also have distinct differences. Here’s how they are similar and how they differ:

Unique Elements:

A set contains only unique values. Duplicate values are not allowed in a set.
A dict contains key-value pairs, where each key must be unique. If you add a key with a different value, the existing value for that key will be updated.
Data Structure:

A set is an unordered collection of values, meaning that the elements do not have a specific order.
A dict is a collection of key-value pairs, where each key is associated with a value. The keys in a dictionary are unique and used to access their corresponding values.
Unique Keys:

In a dict, keys must be unique. If you insert a key that already exists with a new value, the old value will be replaced.
In a set, there are no keys, just values, and each value must be unique.
Accessing Values:

In a set, you can check if a value exists, but you cannot access elements by index.
In a dict, you can access values using their keys. Keys serve as "addresses" for the values in the dictionary.

"""
