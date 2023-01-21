import xlwings as xw

" Hàm tìm dòng cuối dữ liệu --->int"
def get_last_row (obj_sheet, col_name): 
    obj_last_Cells = obj_sheet.cells.last_cell#1048567    
    lr_sh = obj_last_Cells.row
    lr_data = obj_sheet.range(col_name+str(lr_sh)).end('up').row    
    return lr_data

" Hàm tìm số cột cuối dữ liệu --->int" 
def get_last_column (obj_sheet, num_row):    
    obj_last_Cells = obj_sheet.cells.last_cell#1048567
    lc_sh = obj_last_Cells.column
    lc_data = obj_sheet.range(num_row, lc_sh).end('left').column    
    return lc_data

"Thuật toán đổi số cột thành tên cột"
def covert_colNum_into_colName(iCol):    
    tong_so_hang = int(((26-1)/1)+1)    
    col_name =''
    while iCol >0:
        col_name = chr(((iCol-1)%tong_so_hang)+65) + col_name
        steps = (iCol-1)//tong_so_hang
        iCol = steps
    return col_name

" Hàm tìm vùng có chứa dữ liệu --->range" 
def get_have_dataOfRange (obj_sheet:object, Cell_addressFist:str)->object: 
    lc_data = get_last_column (obj_sheet,int(Cell_addressFist[-1]))
    # lc_name = obj_sheet.range(1,lc_data).address.split("$")[1]
    lc_name = covert_colNum_into_colName(lc_data)
    lr = get_last_row(obj_sheet, Cell_addressFist[0])
    str_lr = str(lr)
    rng_Data = shs[0].range(f"{Cell_addressFist}:{lc_name}{str_lr}")
    return rng_Data

"Lấy danh sách tiêu đề return--->list"
def get_list_title(obj_range:object, num_rowOfTitle:int)->list:
    title_list = obj_range.value[:num_rowOfTitle]      
    return title_list

"filter_data_remove_empty_rows return list"
def filter_data_remove_empty_rows(obj_range, num_rowOfTitle:int)->list:    
    data_list = obj_range.value[num_rowOfTitle:]    
    out_list =[]    
    for i_row in range (len(data_list)):
        if data_list[i_row][0] != None and not isinstance(data_list[i_row][0], str): 
            out_list.append(data_list[i_row])
    return out_list
""
"conection data_title and data_list--->list"
def conect_titleAndData(obj_range:object, num_rowOfTitle:int)->list:
    list_titleAndData = []
    list_title = get_list_title(obj_range, num_rowOfTitle)
    list_titleAndData.extend(list_title)    
    list_data = filter_data_remove_empty_rows(obj_range, num_rowOfTitle)   
    list_titleAndData.extend(list_data)    
    return list_title, list_data, list_titleAndData

"get cluster "
def get_clusterOfData(list_data:list, cluster_num:int)->list:
    n = len(list_data)
    n_int = n // cluster_num
    n_odd = n % cluster_num
    group_list = []
    for i_n in range(cluster_num):
        begin = i_n*n_int
        after = begin + n_int
        list_cluster_i = list_data[begin:after]
        group_list.append(list_cluster_i)
        print(f"Nhóm{i_n+1}")
        print(group_list[i_n])
    "Nhóm cuối cùng"
    i_n +=1
    begin = after
    after = begin + n_odd
    group_list.append(list_data[begin:after])
    print(f"Nhóm{i_n+1}")
    print(group_list[i_n])
    return group_list

in_path = r'E:\py_Excel\File_Code\excel\cluster.xlsx'#DanhSach.xlsx'
book = xw.Book(in_path)
shs = book.sheets

"1.Tìm vùng có chứa dữ liệu qua từng sheets"
rg = get_have_dataOfRange (shs[0], "A3")
# print(rg)

title, data , conect_data = conect_titleAndData(rg, 2)
# print(data)
group = get_clusterOfData(data, 2)
# print('Số nhóm')
# print(len(group))
# shs('result').range('A40').value = group

