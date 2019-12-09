import pandas as PD

file_path="D:\\Pythonpractice\\Book1.xlsx"

read_data=PD.read_excel(file_path,sheet_name='Sheet3')
print('Print all the column names before renaming ')
print(read_data.columns)

print('Print all the column names after renaming ')
read_data.columns=['Type1','Customer1','Project1','Task2']

print(read_data.columns)

print(read_data)




