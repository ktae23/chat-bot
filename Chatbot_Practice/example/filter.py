def is_even(number):
    return number % 2 == 0

nubmers = range(1, 21)
print(list(filter(is_even, nubmers)))
