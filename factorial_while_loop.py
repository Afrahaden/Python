def factorial(n):
    if n == 0:
        return 1
    elif n < 0:
        print("Sorry, factorial does not exist for negative numbers")
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))