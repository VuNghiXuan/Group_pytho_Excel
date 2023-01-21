"1. Tìm hiểu về hàm ord: Numerical order, ASCII"
# print(ord("AA"))
"Dãy số 1, 2, 3,..., 25, 26"
"Dãy số 1, 3, 5"
# tong_so_hang = ((5-1)/2)+1


def get_colname_Excel(iCol):
    tong_so_hang = int(((26-1)/1)+1)    
    col_name =''
    while iCol >0:
        col_name = chr(((iCol-1)%tong_so_hang)+65) + col_name
        steps = (iCol-1)//tong_so_hang
        iCol = steps    
    return col_name

def get_AllColNames_Excel():
    list_ColName = []
    for i_name in range(0,16384):
        colname = get_colname_Excel(i_name+1)        
        list_ColName.append(colname)
    return list_ColName 

import tkinter as tk
from tkinter import ttk
  
# Creating tkinter window
window = tk.Tk()
window.title('App"s" VuNghiXuan')
window.geometry('500x250')
  
# label text for title
ttk.Label(window, text = "Hãy chọn tên cột", 
          background = 'green', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)
  
# label
ttk.Label(window, text = "Click dropdown:",
          font = ("Times New Roman", 10)).grid(column = 0,
          row = 5, padx = 10, pady = 25)
  
# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] =  get_AllColNames_Excel()
  
monthchoosen.grid(column = 1, row = 5)
monthchoosen.current(0)
window.mainloop()
