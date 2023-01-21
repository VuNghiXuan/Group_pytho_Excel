import xlwings as xw

def get_last_row (obj_sheet, col_name):    
    
    obj_last_Cells = obj_sheet.cells.last_cell#1048567
    print("Địa chỉ ô cuối của Bảng tính Excel", obj_last_Cells)

    lr_sh = obj_last_Cells.row
    # print("Dòng cuối của Bảng tính Excel", lr_sh)

    lr_data = obj_sheet.range(col_name+str(lr_sh)).end('up').row
    # print(lr_data)

    return lr_data

in_path = r'E:\py_Excel\File_Code\excel\DanhSach.xlsx'

book = xw.Book(in_path)

shs = book.sheets
# print(shs)

sh1 = shs[0]
# print(sh1)

"1.Tìm dòng cuối dữ liệu bằng phương thức down"
lr_down = sh1.range('B5').end('down').row

print("lr_down là:",lr_down)

"2.Tìm dòng cuối dữ liệu bằng phương thức up"
# lr_data = get_last_row(sh1, "C")
# print(lr_data)

"3.Tìm dòng cuối dữ liệu qua từng sheets"
for sh in book.sheets:
    lr = get_last_row(sh, "C")
    print('Tên sheet:',sh.name,". Dòng cuối là: ", lr)