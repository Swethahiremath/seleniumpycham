#Print the total number of rows and columns in a sheet 
import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

a=PD.read_excel(file_path,sheet_name='Sheet1')

s=a.shape

print('Total no of rows and columns in sheet is ',s)


