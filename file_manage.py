from time import time
import os

f = open('data/newfile.txt', 'w')
for i in range(11):
    data = '%d번째 줄입니다.\n' % i
    f.write(data)
f.close()

# readline_test.py
f = open('data/newfile.txt', 'r')
line = f.readline()
print(line, 'readline')
f.close()

# readline_all.py
f = open('data/newfile.txt', 'r')
while True:
    line = f.readline()
    if not line : break
    print(line, 'readline_all')
f.close()

# adddata.py
f = open("data/newfile.txt",'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()


while 1:
    data = input()
    if not data : break
    print(data)

# readlines.py
f = open('data/newfile.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line, end=' ')
    print('readlines')
f.close()

# read.py
f = open('data/newfile.txt', 'r')
data = f.read()
print(data, 'read')
f.close()





# path = os.getcwd()
# file_name = path + '/' + 'data/portfolio.csv'
# start = time()
# f = open('data/newfile.txt', 'rt')
# data = f.read()
# f.close()
# data
# duration = time() - start
# print(data, duration)
# duration = time() - start
# print(duration)


# start = time()
# with open('data/dowstocks.csv', 'rt') as file:
#     for line in file:
#         # data = file.read()
#         print(line)
# duration = time() - start
# print(duration)
# print(os.getcwd())

# class file_control():

#     def file_open(file_name):
#         data = []
#         with open(file_name, 'rt') as f:
#             for line in f:
#                 data.append(line)
#         return data

#     def file_write(data):
#         with open('outfile', 'wt') as out:
#             out.write(data)



#     def headers(data):
#         headers = next(data)
#         return headers

#     def print(data):
#         for d in data:
#             print(d)


# data = file_control.file_open('data/dowstocks.csv')
# # header = file_control.headers(data)
# file_control.print(data)
# file_control.file_write(data)







