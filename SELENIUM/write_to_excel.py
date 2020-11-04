import openpyxl

path = r"C:\Users\Majster\Desktop\IEPS\PYTHON\SELENIUM\data2.xlsx"

workbook = openpyxl.load_workbook(path)

sheet = workbook.active

for r in range(1,5):
    for c in range(1,4):
         sheet.cell(r,c).value = "Welcome"

workbook.save(path)
