import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet['A1'] = 200               #Set the cell value
sheet['A2'] = 300               #Set the cell value
sheet['A3'] = '=SUM(A1:A2)'     #Set the formula
wb.save('writeFormula.xlsx')