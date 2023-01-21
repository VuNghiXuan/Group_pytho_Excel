from matplotlib import pyplot as plt
import xlwings as xw

# Plot 1
x = [2, 4, 6]
y = [8, 10, 12]

img= plt.figure()
plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("Biểu đồ 1")

# Plot 2
a = [3, 5, 7]
b = [9, 11, 12]

# img= plt.figure()
plt.subplot(1, 2, 2)
plt.bar(a,b)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Biểu đồ 2")

pic = plt.savefig(r'C:\Users\DELL\Desktop\plotlib.jpg')
book = xw.Book(r'C:\Users\DELL\Desktop\matplotlib.xlsx')
sh = book.sheets[0]
rng = sh.range('B5')
# sh1.pictures.add(img, name = "1",update = True )
sh.pictures.add(r'C:\Users\DELL\Desktop\plotlib.jpg',name = "my", top=rng.top, update = True)
plt.suptitle('Biểu đồ')
# plt.show()