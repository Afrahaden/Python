# ternary operators
is_friend = True
can_message = 'Message allowed.' if is_friend else 'not allowed to message'

print(can_message)

# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
minimum = a if a < b else b

print(minimum)
