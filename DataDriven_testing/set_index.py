#program to add two sheets using concat function
import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

excel_sheet1=PD.read_excel(file_path,sheet_name='Sheet1')

data=excel_sheet1.set_index('name',inplace=True)
print(data)