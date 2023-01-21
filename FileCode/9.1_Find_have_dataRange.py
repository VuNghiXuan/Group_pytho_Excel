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
"&AA&3"
" Hàm tìm vùng có chứa dữ liệu --->range" 
def get_have_dataOfRange (obj_sheet, Cell_addressFist): 
    lc_data = get_last_column (obj_sheet,int(Cell_addressFist[-1]))
    lc_name = obj_sheet.range(1,lc_data).address[1]
    lr = get_last_row(obj_sheet, Cell_addressFist[0])
    str_lr = str(lr)
    rng_Data = shs[0].range(f"{Cell_addressFist}:{lc_name}{str_lr}")

      
    return rng_Data


in_path = r'E:\py_Excel\File_Code\excel\DanhSach.xlsx'
book = xw.Book(in_path)
shs = book.sheets

"1.Tìm vùng có chứa dữ liệu qua từng sheets"
rg = get_have_dataOfRange (shs[0], "A3")
print(rg)






