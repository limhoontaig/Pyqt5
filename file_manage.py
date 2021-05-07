from time import time
import os

# path = os.getcwd()
# file_name = path + '/' + 'data/portfolio.csv'
# start = time()
# f = open(file_name, 'rt')
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

class file_control():

    def file_open(file_name):
        data = []
        with open(file_name, 'rt') as f:
            for line in f:
                data.append(line)
        return data

    # def headers(data):
    #     headers = next(data)
    #     return headers

    def print(data):
        for d in data:
            print(d)


data = file_control.file_open('data/dowstocks.csv')
# header = file_control.headers(data)
file_control.print(data)






