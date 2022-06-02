import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
print(tuple(sheet['A1':'C3'])) # Get all cells from A1 to C3.


for rowOfCellObjects in sheet['A1':'C3']:   # Goes over each row in the slice
    for cellObj in rowOfCellObjects:        # Goes over each cell in the above row
        print(cellObj.coordinate, cellObj.value)  # All of the columns of the selected row are printed
    print('--- END OF ROW ---')