from openpyxl import load_workbook
wb = load_workbook("sample_formula.xlsx", data_only=True)
ws = wb.active


#  수식 그대로 가져오고 있음
# evaluate 되지 않은 상태에서의 데이터에는 None이라고 표시 >> 사람이 직접열어서 한번 저장해주어야 수식이 적용된 값 출력 가능
for row in ws.values:
    for cell in row:
        print(cell)
