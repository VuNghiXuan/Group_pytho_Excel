"1. Thư viện matplotlib: trực quan hóa dữ liệu"
import xlwings as xw
from matplotlib import pyplot as plt
x = [1, 5, 8]
y = [3, 7, 12]

a = [2, 6, 6]
b = [4, 8, 12]

img = plt.figure()
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Biểu đồ 1")

plt.subplot(1,2,2)
plt.plot(a,b)
plt.title("Biểu đồ 2")

book = xw.Book()
sh = book.sheets[0]
"cách 1"
# sh.pictures.add(img, name = "chart", update =True)
plt.savefig(r"E:\py_Excel\File_Code\excel\chrt.png")
sh.pictures.add(r"E:\py_Excel\File_Code\excel\chrt.png", name = "chart", update =True)
# plt.show()
