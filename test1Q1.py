a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def only_even(x):
    return [a for a in x if a%2 == 0]

print(only_even(a))