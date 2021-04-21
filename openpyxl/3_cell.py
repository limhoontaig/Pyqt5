from random import *
from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "NadoSheet"

# A1셀에 1이라는 값 입력

ws["A1"] = 1
ws["A2"] = 2
ws["A3"] = 3
ws["B1"] = 4
ws["B2"] = 5
ws["B3"] = 6

print(ws["A1"].value)  # 셀 A1의 value 출력
print(ws["A10"].value)  # 값이 없을 떈 'None' 출력
print(ws.cell(column=1, row=1).value)  # ws["A1"].value 와 같은 값이다.
print(ws.cell(column=2, row=1).value)  # ws["B1"].value 와 같은 값이다.

for x in range(1, 11):
    for y in range(1, 11):
        ws.cell(row=x, column=y, value=randint(0, 100))


wb.save("cell.xlsx")
wb.close()
