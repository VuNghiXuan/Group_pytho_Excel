import xlwings as xw


book = xw.Book(r'E:\py_Excel\File_Code\excel\ThongKe_QuanAo.xlsx')

# Lấy dữ liệu vùng từ bảng tính Excel
data_request = book.sheets('data_request').range('A2:E17').value

total_row = len(data_request)
# total_col = len(data_request[0])
range_out_data = []

for i_row in range(total_row):
    if data_request[i_row][0] == "ÁO" or data_request[i_row][0] == "QUẦN":
        list_1d = [0,0,0,0]
        list_1d[0] = data_request[i_row][0] #Kiểu 
        list_1d[1] = data_request[i_row][1] # Màu
        list_1d[2] = data_request[i_row+1][1] # size
        list_1d[3] = data_request[i_row+2][1] # số lượng

        # Add vào range_out_data
        range_out_data.append(list_1d)

        # add sixe M
        list_1d = [0,0,0,0]
        list_1d[0] = data_request[i_row][0] #Kiểu 
        list_1d[1] = data_request[i_row][1] # Màu
        list_1d[2] = data_request[i_row+1][2] # size
        list_1d[3] = data_request[i_row+2][2] # số lượng
        range_out_data.append(list_1d)

        # add sixe L
        list_1d = [0,0,0,0]
        list_1d[0] = data_request[i_row][0] #Kiểu 
        list_1d[1] = data_request[i_row][1] # Màu
        list_1d[2] = data_request[i_row+1][3] # size
        list_1d[3] = data_request[i_row+2][3] # số lượng
        range_out_data.append(list_1d)

        # add sixe XL
        list_1d = [0,0,0,0]
        list_1d[0] = data_request[i_row][0] #Kiểu 
        list_1d[1] = data_request[i_row][1] # Màu
        list_1d[2] = data_request[i_row+1][4] # size
        list_1d[3] = data_request[i_row+2][4] # số lượng
        range_out_data.append(list_1d)

        
        # print(range_out_data)



    # for i_col in range(total_col):
    #     print(data_request[i_row][i_col])        
# print(data_request)
title = ["KIỂU","MÀU","SIZE","TOTAL"]
range_out_data.insert(0, title)

book.sheets('data_request').range('H5').value = range_out_data
