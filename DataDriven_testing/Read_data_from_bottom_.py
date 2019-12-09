import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

a=PD.read_excel(file_path)

#Data from bottom last 5 data
#print(a.tail())

# Data from bottom last 2 data
print(a.tail(2))
