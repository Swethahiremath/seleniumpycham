from  DataDriven_testing.Login_using_excel_actitim import login

from DataDriven_testing import excel_methods as excel

file_path="D:\\Pythonpractice\\login_credit.xlsx"

rows=excel.get_row(file_path,"Sheet1")

for i in raange(0,rows):
    username=excel.get_deta(file_path,"Sheet1",i,"usename")
    password=excel.get_deta(file_path,"Sheet1",i,"pwd")
    expected_result=excel.get_data(file_path,"Sheet1",i,"Expected_result")

    status=login(username,Password,expected_result)

    if status:
        excel.write_to_excel(file_path,"Sheet1",i,"Result","TEST_PASS")
    else:
        excel.write_to_excel(file_path,"Sheet1",i,"Result","TEST_PASS")


