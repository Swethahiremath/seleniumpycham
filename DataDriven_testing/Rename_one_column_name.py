import pandas as PD

file_path="D:\\Pythonpractice\\Book1.xlsx"

read_data=PD.read_excel(file_path,sheet_name='Sheet3')
print('Print all the column names before renaming ')
print(read_data.columns)


print('rename one column name ')
updated_column=read_data.rename(columns={'Customer':'Customer2'})

print(updated_column)