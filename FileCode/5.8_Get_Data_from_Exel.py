import xlwings as xw

path_file = r'E:\py_Excel\File_Code\excel\obj_range.xlsx'
book  = xw.Book(path_file)

# book.save(r'E:\py_Excel\File_Code\excel\obj_range.xlsx')
shs = book.sheets

sh1 = shs[0]
# print(sh1.name)

# Cách lấy dữ liệu từ bảng tính excel lưu vào biến python
get_Data = sh1.range('A10:C12').value

print(get_Data)

# Tìm mối liên hệ id list Python và cột, dòng bảng Excel
print("Dòng đầu tiên", get_Data[0])
print("Dòng cuối", get_Data[-1])

print("Dòng đầu tiên, cột thứ 2, có giá trị là", get_Data[0][1])
print("Dòng thứ 2, cột thứ 1, có giá trị là", get_Data[1][0])