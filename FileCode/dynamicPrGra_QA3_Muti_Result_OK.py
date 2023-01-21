"Input"
rng = [2, 3, 4, 1]
S = 5 #Tổng cần tìm

"Phương án truy vết nhiều kết quả"
row = len(rng)
col = S+1

pa = [0]*col
# pa[0]=1

"Phân biệt vùng trỏ"
pa = [[0 for _ in range(col)] for _ in range(row)]
for i in range(len(pa)):
    pa[i][0]=1

hieu = [["" for _ in range(col)] for _ in range(row)]
print("pa:------  '\n'")
print(pa)
print(hieu)


# for i in range(len(rng)):
#     for j in range(S, rng[i]-1,-1):   
#         if pa[i][j]==0 and pa[i][j-rng[i]]==1:
#             pa[i][j]=1
#             hieu[i][j] = j-rng[i] 

# for i in range(len(rng)):
#     for j in range(S, rng[i]-1,-1):
#         # Viết cho nhiều phương án có tổng bằng S  
#         if pa[j]==1 and j==S:
#             if pa[j-rng[i]]==1:
#                 pa[j]=1
#                 hieu[i][j] = j-rng[i] 
#             # if i==2 and  j==4:
#             #     print(hieu[i][j])
#             # print(i,j,"  ", j-rng[i] )
#         # Giữ như cũ thay if == elif  
#         elif pa[j]==0 and pa[j-rng[i]]==1:
#             pa[j]=1
#             hieu[i][j] = j-rng[i] 

# print(pa)
# print(hieu)

# if pa[S]!=1:
#     print(f"Không có phương án {S} là+'\n'")
# else:
#     # Viết cho nhiều phương án có tổng bằng S 
#     len_hieu = len(hieu)
#     for i_hieu in range(len_hieu):
#         if hieu[i_hieu][S]!="":

#             result=[]    
#             while S>0:
#                 result.append(S-hieu[i_hieu][S])
#                 S = hieu[i_hieu][S]  

    
# print(result)

