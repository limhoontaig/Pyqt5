from openpoyxl import Workbook

# Workbook create
wb = Workbook() #
ws = wb.active # open active sheet
ws.title = "LHTSheet"
wb.save('sample.xlsx')
wb.close()

# wb.copy_worksheet

