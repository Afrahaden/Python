def star_end_decorator(func):
    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


@star_end_decorator
def print_name():
    print("Afrah")


# print_name = star_end_decorator(print_name)
print_name()
