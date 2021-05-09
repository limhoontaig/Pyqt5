def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

avg = avg_numbers(1,2,3,4,250005)
print('avg = avg_numbers(1,2,3,4,250005)', avg)

# avg = avg_numbers(1,3,5,7,9,11,13,15,17,19,20)
# print('l = [1,3,5,7,9,11,13,15,17,19,20]', avg)