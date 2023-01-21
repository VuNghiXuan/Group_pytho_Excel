# Kiểu dữ liệu list:
my_list = ['Nguyễn Văn A', 'Lê Văn Tám', 1587]

# Cách 1: lấy giá trị từng phần tử trong list
# for li in my_list:
#     print(li)

# Cách 2: lấy giá trị từng phần tử trong list
# sum_elOflist = len(my_list)
# print(sum_elOflist)

# for id_li in range(sum_elOflist):
#     print("index trong My_list:", id_li)
#     print(" Giá trị tương ứng với id là: ",my_list[id_li])

# print("My list đầu tiên", my_list)

# my_list[2] = "Trần Thay Đổi"
# print("My list sau khi thay đổi", my_list)

# Cách thay đổi giá trị trong list
print("List ban đầu", my_list)

# print("Giá trị cần thay đổi là: ", my_list[2])
# my_list[2] = "Trần Thay Đổi"
# my_list[-1] = "Trần Thay Đổi"
# print("List sau khi thay đổi", my_list)

# Cách tìm id từ giá trị đã biết
find_id = my_list.index('Lê Văn Tám')
print(find_id)


