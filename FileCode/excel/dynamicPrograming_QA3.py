# "Step 1: Khởi tạo"
# day_so = [2, 8, 4]
# tong_can_tim = 5 #Tổng cần tìm
# # day_so.sort()
# # print(day_so)
# """
# ? Bài toán đặt ra tìm nghiệm x+ số mấy = 5 ==>x = 5 - số mấy
# Nghĩa là ==> x = 5 - a[i]
# """
# # pa = [0]*(k+1)
# pa = [0]*(tong_can_tim+1)
# pa[0] = 1
# # print(pa)
# hieu = [""]*(tong_can_tim+1)

# # print(hieu, pa)
# for i in range(len(day_so)):
#     # print(day_so[1])
#     for j in range(len(pa)-1, day_so[i]-1,-1): #day_so[i]-1 
#         # print(day_so[i]-1)      
#         if pa[j]==0 and pa[j-day_so[i]]==1:
#             pa[j]=1
#             hieu[j] = j-day_so[i]            
# print(pa)    
# if pa[tong_can_tim]!=1:print(f"Không có phương án {tong_can_tim} là+'\n'")
# else:
#     out=[]
#     n=tong_can_tim
#     while n>0:
#         # print(n-hieu[n], end = ' ')
#         n = hieu[n]
for i in range(5,1,-1): 
    print(i)