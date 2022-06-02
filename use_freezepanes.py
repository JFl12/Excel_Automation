import openpyxl

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active
sheet.freeze_panes = 'A2'   #Freeze the rows above A2 (the headers will always be visable)
wb.save('freezeExample.xlsx')