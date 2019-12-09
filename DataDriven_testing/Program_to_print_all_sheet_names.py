import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

x1=PD.ExcelFile(file_path)
total_sheet=x1.sheet_names

for sheet in total_sheet:
    print(sheet)

