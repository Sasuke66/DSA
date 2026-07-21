# Simple implementation of a hash map in Python
hash_map = {}

# Adding key-value pairs to the hash map
hash_map['name'] = 'John Doe'
hash_map['age'] = 30

# Retrieving values from the hash map
name = hash_map.get('name')
print(name)  # Output: John Doe

# Checking if a key exists in the hash map
if 'age' in hash_map:
    age = hash_map['age']
    print(age)  # Output: 30

# Removing a key-value pair from the hash map
del hash_map['name']

# Displaying the contents of the hash map
print(hash_map)  # Output: {'age': 30}

## Note: This is a simple implementation using Python's built-in dictionary.