import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

x1=PD.ExcelFile(file_path)
total_sheet=len(x1.sheet_names)
print('Print the data',total_sheet)
