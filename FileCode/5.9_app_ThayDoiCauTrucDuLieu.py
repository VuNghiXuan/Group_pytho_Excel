import xlwings as xw


book = xw.Book(r'E:\py_Excel\File_Code\excel\ThongKe_QuanAo.xlsx')

# Lấy dữ liệu vùng từ bảng tính Excel
data_request = book.sheets('data_request').range('A2:E17').value

total_row = len(data_request)
total_col = len(data_request[0])


for i_row in range(total_row):
    print(data_request[i_row])
    for i_col in range(total_col):
        print(data_request[i_row][i_col])        
# print(data_request)

