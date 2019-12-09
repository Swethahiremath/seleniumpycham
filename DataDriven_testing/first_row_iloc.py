#program to add two sheets using concat function
import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

excel_sheet1=PD.read_excel(file_path,sheet_name='Sheet1')
# print data in row wise
#values=excel_sheet1.iloc[0]

#print 2nd row data
values=excel_sheet1.iloc[1]

#ptogram to selecct last row
values=excel_sheet1.iloc[-1]


print(values)