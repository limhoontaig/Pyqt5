def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(9))
print(is_odd(8))

is_odd = lambda x: True if x % 2 == 1 else False

print(is_odd(4))
print(is_odd(8))

