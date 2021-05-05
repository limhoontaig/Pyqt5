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
#     print(i,'*',dan,'=',i*dan)#,end=' ')

# Example 8
# f = open('abc.txt', 'r', encoding='UTF-8')
# lines = f.readlines()
# f.close()

# lines.reverse()

# f = open('abc.txt','w',encoding = 'UTF-8')
# for line in lines:
#     line = line.strip()
#     print(line)
#     f.write(line)
#     f.write('\n')

# f.close()

# Example 9

# f = open('sample.txt','r')
# lines = f.readlines()
# f.close()
# total = 0
# i = 0
# for n in lines:
#     total += int(n)
#     i += 1
# average = total / len(lines)
# print('Total =', total,'Avergae = ',average, total / i)

# f = open('result.txt','a')

# for line in lines:
#     f.write(line)
# f.write('\n')
# f.write('Average : %d\n' % average)
# f.write('Total : %d\n' % total)

# Example 10

# class Calculator:
#     def __init__(self, numberlist):
#         self.numberlist = numberlist
    
#     def sum(self):
#         result = 0
#         for num in self.numberlist:
#             result += num
#         return result
    
#     def avg(self):
#         total = self.sum()
#         return total / len(self.numberlist)

# call1 = Calculator([1,2,3,4,5,0.222,0.546])
# print(call1.sum())
# print(call1.avg())

# call2 = Calculator([6,7,8,9,10,1000,50000])
# print(call2.sum())
# print(call2.avg())

# Example 11 Module Path
# import sys method
# import sys
# sys.path.append('c:/resource/PyQt5')
# import mymod

# PythonPath 환경변수 사용하기
# c:\resource\PyQt5>set PYTHONPATH =c:\resource\PyQt5

# to operate python on python program module in directory

# Example 12

# result = 0
# try:
#     [1,2,3][3]
#     'a' + 1
#     4 / 0
# except TypeError:
#     result += 1
# except ZeroDivisionError:
#     result += 2
# except IndexError:
#     result += 3
# finally:
#     result += 4
# print(result)

#Example 13 Dashinsert function
 
# data = '454679358966842358'
# numbers = list(map(int, data))
# result = []
# print(numbers)

# for i, num in enumerate(numbers):
#     result.append(str(num))
#     if i < len(numbers)-1:
#         is_odd = num % 2 == 1
#         is_next_odd = numbers[i+1] % 2 == 1
#         if is_odd and is_next_odd:
#             result.append('-')
#         elif not is_odd and not is_next_odd:
#             result.append('*')
# print(result)
# print(''.join(result))

# Example 14 compress string

# def compress_string(s):
#     _c = ''
#     cnt = 0
#     result = ''
#     for c in s:
#         if c!=_c:
#             _c = c
#             if cnt: result += str(cnt)
#             result += c
#             cnt = 1
#         else:
#             cnt += 1
#     if cnt: result += str(cnt)
#     return result
# print(compress_string('aaabbcccccca'))

# Example 14 Duplicate numbers

def chkDupNum(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
            #print(result)
        else:
            return False
    #print(result)
    return len(result) == 10

print(chkDupNum('0123456789'))
print(chkDupNum('01234'))
print(chkDupNum('01234567890'))
print(chkDupNum('6789012345'))
print(chkDupNum('012322456789'))
        