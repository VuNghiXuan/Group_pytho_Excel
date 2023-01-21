import xlwings as xw

" Hàm tìm dòng cuối dữ liệu --->int"
def get_last_row (obj_sheet, col_name):    
    
    obj_last_Cells = obj_sheet.cells.last_cell#1048567
    print("Địa chỉ ô cuối của Bảng tính Excel", obj_last_Cells)
    lr_sh = obj_last_Cells.row
    lr_data = obj_sheet.range(col_name+str(lr_sh)).end('up').row    
    return lr_data

" Hàm tìm số cột cuối dữ liệu --->int" 
def get_last_column (obj_sheet, num_row):    
    
    obj_last_Cells = obj_sheet.cells.last_cell#1048567
    print("Địa chỉ ô cuối của Bảng tính Excel", obj_last_Cells)
    lc_sh = obj_last_Cells.column
    lc_data = obj_sheet.range(num_row, lc_sh).end('left').column    
    return lc_data


in_path = r'E:\py_Excel\File_Code\excel\DanhSach.xlsx'
book = xw.Book(in_path)
shs = book.sheets

"1.Tìm dòng cuối dữ liệu qua từng sheets"
# for sh in shs:
#     lr = get_last_column(sh, "C")
#     print('Tên sheet:',sh.name,". Dòng cuối là: ", lr)

obj_last_Cells = shs[0].cells.last_cell#1048567
print(obj_last_Cells.column)

# print(shs[0].range("G7").address)
# print(shs[0].range(5, obj_last_Cells.column).address)

print(get_last_column (shs[0], 5))




