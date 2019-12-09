import pandas as PD

file_path="D:\\Pythonpractice\\Book1.xlsx"

read_data=PD.read_excel(file_path,sheet_name='Sheet3',index_col='Type')
row_value=read_data.loc['General','Customer']

print('Read the data from row and column where we need to write the data ')
print(row_value)
row_value=read_data.loc['General','Customer']='Testing'
writer =PD.ExcelWriter(file_path)
read_data.to_excel(writer,sheet_name='Sheet3')



writer.save()
