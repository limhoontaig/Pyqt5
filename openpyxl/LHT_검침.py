# import os
# from tkinter import *
# from tkinter import filedialog

# from openpyxl import load_workbook  # 파일 불러오기

# def Load():
#     filename = filedialog.askopenfilename(initialdir="/", title="Select file",
#                                           filetypes=(("Excel files", "*.xls, *.xlsx"),
#                                           ("all files", "*.*")))
#     return filename

# filename = Load()





# wb = load_workbook(filename)
# ws = wb.active

# # cell 데이터 불러오기
# for x in range(1, 11):
#     for y in range(1, 11):
#         print(ws.cell(row=x, column=y).value, end=" ")
#     print('/n/n/n/n')


# # cell 갯수를 모를 때
# for x in range(1, ws.max_row + 1):
#     for y in range(1,  ws.max_row + 1):
#         print(ws.cell(row=x, column=y).value, end=" ")
#     print()


# station = ['사당','신도림','인천공항']

# for i in station:
#     print(i+'행 열차가 들어오고있습니다.')


from random import *

for i in range(11):
    print(randint(1,10))

