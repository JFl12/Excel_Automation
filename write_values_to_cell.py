import openpyxl

wb = openpyxl.Workbook()
sheet = wb['Sheet']
sheet['A1'] = 'Hello,world!'    #Edit the cell's value.
print(sheet['A1'].value)