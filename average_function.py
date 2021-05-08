def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

avg = avg_numbers(1,2,3,4,250005)
print(avg)