#program to add two sheets using concat function
import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

excel_sheet1=PD.read_excel(file_path,sheet_name='Sheet1')

print("Before Sorting")
print(excel_sheet1)

print("-----------------------------------------------------")

print("After sorting")

#sortdata=excel_sheet1.sort_values('name',ascending=True)
sortdata=excel_sheet1.sort_values('name',ascending=False)

print(sortdata)