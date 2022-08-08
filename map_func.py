def myfunc(a, b):
    return a + b


x = map(myfunc, (1, 2, 3), (4, 8, 10))

print(x)

# convert the map into a list, for readability:
print(list(x))
