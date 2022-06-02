import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
print(wb.sheetnames)       # The workbook's sheet's names.

sheet = wb['Sheet3'] # Get a sheet from the workbook.
print(sheet)
print(type(sheet))

print(sheet.title)     # Get the sheet's title as a string.

anotherSheet = wb.active    # Get the active sheet.
print(anotherSheet)
