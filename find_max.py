def find_largest(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num
