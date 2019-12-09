#program to slice the row from 2nd to 4th row

#program to add two sheets using concat function
import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

excel_sheet1=PD.read_excel(file_path,sheet_name='Sheet1')
total=excel_sheet1.shape

print(total)

row1=total[0]
colu=total[1]

for i in range(0,row1):
    for j in  range(0,colu):
        value=excel_sheet1.iloc[i,j]
        print(value)



