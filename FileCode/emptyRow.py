import xlwings as xw

"1.Input"
in_path = r'E:\py_Excel\File_Code\excel\remove_empty_rows.xlsx'
book = xw.Book(in_path)
shs = book.sheets

rng = shs[0].range("A1:A27").value
print(rng)
# row_1 = shs[0].range("29:29").api.Delete()
# print(row_1.address)

"Cách xóa nhiều dòng trống"
# for i_row in range(len(rng)-1, -1, -1): 
#     if rng[i_row] == None:           
#         r = i_row+1       
#         row = shs[0].range(f"{r}:{r}").api.Delete()
        # print(shs[0].range(f"{r}:{r}").address)

" Cách xóa cột"

# shs[1].range("B:E").api.Delete()
