from openpyxl import load_workbook, Workbook
def read_from_xl(file_name, sheet_number = 0):
    workbook = load_workbook(file_name)
    sheet = workbook.get_sheet_names()[sheet_number]
    worksheet = workbook.get_sheet_by_name(sheet)
    rows = []
    for row in worksheet.iter_rows():
        cells = []
        for cell in row:
            cells.append(cell.value)
        rows.append(cells)
    workbook.save(file_name)
    return rows

a = read_from_xl('Date.xlsx')
print(a)
for i in a:
    print(i)
        
