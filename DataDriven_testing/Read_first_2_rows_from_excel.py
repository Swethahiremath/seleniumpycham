import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

a=PD.read_excel(file_path)

print(a.head(2))
