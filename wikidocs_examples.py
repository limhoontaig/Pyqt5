# Jump to Python Chapter 8
# Example 1
# txt = 'a:b:c:d'
# tx = txt.split(':')
# print(tx)
# tx1 = '#'.join(tx)
# print(tx1)

# Example 2
# a = {'C':90,'B':80}
# c = a.get('C',70)
# a = a.get('A',85)
# # a['A']
# print(c)
# print(a)

# Example 3
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# # b = 0
# # for a in A:
# #     if a > 50:
# #         b = b + a
# #     else:
# #         pass
# # print(b)

# result = 0
# while A:
#     mark = A.pop()
#     if mark >= 50:
#         result += mark

# print(result)

# Example 5

# pinabocci = input('피나보치 함수를 구할 수를 입력하세요 :')
# a = 0
# b = 1 
# while b < pinabocci:
#     b = a + b
#     b 
# import time
# def fib(n):
#     if n == 0 : return 0
#     if n == 1 : return 1
#     return fib(n-2) + fib(n - 1)

# for i in range(11):
#     start = time.time()
#     print(i, fib(i))
#     print('time:', time.time() - start)

# Example 6
# import time

# user_input = input('숫자를 입력하세요 :')
# numbers = user_input.split(',')
# total = 0
# start = time.time()
# for n in numbers:
#     total += int(n)
# t = time.time() - start
# print(total, t)

# Example 7

# user_input = input('구구단을 출력할 숫자를 입력 하세요(2~9):')
# dan = int(user_input)
# for i in range(1, 10):
#     print(i,'*',dan,'=',i*dan,end=' ')

# Example 8
f = open('abc.txt', 'r')
lines = f.readlines()
f.close()

lines.reverse()

f = open('abc.txt','w')
for line in lines:
    line = line.strip()
    f.write(line)
    f.write('/n')
f.close()
