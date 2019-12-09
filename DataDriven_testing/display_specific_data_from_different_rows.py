#program to slice the row from 2nd to 4th row

#program to add two sheets using concat function
import pandas as PD


file_path="D:\\Pythonpractice\\Book1.xlsx"

excel_sheet1=PD.read_excel(file_path,sheet_name='Sheet1')


#values=excel_sheet1.iloc[2:4]

#Program to print seleccted rows
#values=excel_sheet1.iloc[[3,5,6]]
#print(values)

#Program to print the data column wise
#values=excel_sheet1.iloc[:,0]
#print(values)

# Program to selcet the last column of the data fram
#print('Data from the last column')
'''values=excel_sheet1.iloc[:,-1]
print(values)'''

# Program to select first 2 column of the data fram
'''print('Data from the last column')
values=excel_sheet1.iloc[:,0:2]
print(values)'''

# Program to select specific column
'''print('Data from the specific column name and last column ')

values =excel_sheet1.iloc[:,[0,2]]
print(values)'''

# Progfram to select multiple rows and columns using iloc indexer ,here is the program to select 1st 3 rows and columns
'''values=excel_sheet1.iloc[0:3,1:4]
print(values)'''

# Program to print specific row data and column data
values=excel_sheet1.iloc[[0,2,4],[1,3]]
print(values)
