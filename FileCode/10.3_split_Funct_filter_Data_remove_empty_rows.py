import xlwings as xw

"1. Hàm tìm dòng cuối dữ liệu --->int"
def get_last_row (obj_sheet, col_name): 
    obj_last_Cells = obj_sheet.cells.last_cell#1048567    
    lr_sh = obj_last_Cells.row
    lr_data = obj_sheet.range(col_name+str(lr_sh)).end('up').row    
    return lr_data

"2. Hàm tìm số cột cuối dữ liệu --->int" 
def get_last_column (obj_sheet, num_row):    
    obj_last_Cells = obj_sheet.cells.last_cell#1048567
    lc_sh = obj_last_Cells.column
    lc_data = obj_sheet.range(num_row, lc_sh).end('left').column    
    return lc_data

"3.Thuật toán đổi số cột thành tên cột"
def covert_colNum_into_colName(iCol):    
    tong_so_hang = int(((26-1)/1)+1)    
    col_name =''
    while iCol >0:
        col_name = chr(((iCol-1)%tong_so_hang)+65) + col_name
        steps = (iCol-1)//tong_so_hang
        iCol = steps
    return col_name

"4. Hàm tìm vùng có chứa dữ liệu --->range" 
def get_have_dataOfRange (obj_sheet, Cell_addressFist): 
    lc_data = get_last_column (obj_sheet,int(Cell_addressFist[-1]))
    # lc_name = obj_sheet.range(1,lc_data).address.split("$")[1]
    lc_name = covert_colNum_into_colName(lc_data)
    lr = get_last_row(obj_sheet, Cell_addressFist[0])
    str_lr = str(lr)
    rng_Data = shs[0].range(f"{Cell_addressFist}:{lc_name}{str_lr}")
    return rng_Data

"5. Hàm lấy tiêu đề"
def get_list_title(obj_range:object, numTitle:int)->list:
    title_list = obj_range.value[0:numTitle]        
    return title_list

"6. Filter_data_remove_empty_rows"
def filter_data_remove_empty_rows(obj_range, num_Title:int):    
    data_list = obj_range.value[num_Title:]    
    out_list =[]    
    for i_row in range (len(data_list)):
        if data_list[i_row][0] != None and not isinstance(data_list[i_row][0], str): 
            out_list.append(data_list[i_row])
    return out_list

"7. Gộp title và data thành 1--> list2D"
def get_merge_titleAndData(title_list: list, data_list:list)-> list:
    list_merge = []
    list_merge.extend(title_list)
    list_merge.extend(data_list)
    return list_merge

in_path = r'E:\py_Excel\File_Code\excel\DanhSach.xlsx'
book = xw.Book(in_path)
shs = book.sheets

"1.Tìm vùng có chứa dữ liệu qua từng sheets"
rg = get_have_dataOfRange (shs[0], "A3")
li_title = get_list_title(rg, 2)

li_data = filter_data_remove_empty_rows(rg,2)
li_merge = get_merge_titleAndData(li_title,li_data)
print(li_merge)


shs.add("result").range("A1").value = li_merge