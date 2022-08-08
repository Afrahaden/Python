user = {
    'name': 'Afrah',
    'age': 71,
    'can_swim': True
}

# Getting the keys only
for item in user:
    print(item)
print('-------------------------')
# Getting the keys and the values
for item in user.items():
    print(item)
print('-------------------------')
# Getting the values only
for item in user.values():
    print(item)
print('-------------------------')
# Getting the keys only
for item in user.keys():
    print(item)
print('-------------------------')
# Getting the keys and the values in shorthand way
for key, value in user.items():
    print(key, value)
