import functools

my_list = [1, 2, 3]


def accumulator(acc, item):
    print(acc, item)
    return acc + item


print(functools.reduce(accumulator, my_list, 0))
