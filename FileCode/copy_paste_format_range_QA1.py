import xlwings as xw

in_path = r'E:\py_Excel\File_Code\excel\DanhSach.xlsx'
book = xw.Book(in_path)
shs = book.sheets

rng = shs[0].range("A3:E9").copy()
shs("vunghixuan").range("B5").paste('formats')








