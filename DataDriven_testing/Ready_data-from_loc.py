import pandas as PD
import xlrd


file_path="D:\\Pythonpractice\\Book1.xlsx"

execl_sheet1=PD.read_excel(file_path,sheet_name='Sheet3',index_col='Type')

#print particular row and column values
#row_col_values=execl_sheet1.loc['General','Customer']

#print entire row using row name
#row_col_values=execl_sheet1.loc['General']

#print multiple row data using row name
#row_col_values=execl_sheet1.loc[['General','Adminstration']]

#print(row_col_values)

#program to read single column name using column name
#column_data=execl_sheet1.loc[:,['Customer']]

#Program to read multiple data from column using column name
#column_data=execl_sheet1.loc[:,['Customer','Project']]

#program to read cell value using row and column value
print('Data from specific row and column ')
row_col_data=execl_sheet1.loc['General','Customer']
print(row_col_data)


