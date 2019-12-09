import pandas as PD

file_path="D:\\Pythonpractice\\Book1.xlsx"

execl_sheet1=PD.read_excel(file_path,sheet_name='Sheet2')

data_from_row_col=execl_sheet1.loc[0,'name1']

print(data_from_row_col)