#program to add two sheets using concat function
import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

excel_sheet1=PD.read_excel(file_path,sheet_name='Sheet1')
excel_sheet2=PD.read_excel(file_path,sheet_name='Sheet2')

x1_sheet=PD.concat([excel_sheet1,excel_sheet2])




print(x1_sheet)