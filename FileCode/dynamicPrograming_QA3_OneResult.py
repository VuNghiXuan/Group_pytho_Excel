"Input"
rng = [2, 3, 4, 1]
S = 5 #Tổng cần tìm
"""
Step 1: Kiểm tra tồn tại kết quả S-rng[i]
    Ví dụ:
        S-rng[0] = 5-2=3
        3-1=2
        2-1=1
        1-1=0
        . Lấy 3 kiểm tra trong rng có tồn tại số 3 hay không?
        Giả sử tại vị trí rng[1] != 3 mà là rng[1] == 1 ????
        Bài toán quá khó nếu như có rng có n số hạng;
    Cách giải:
        Tổng các số hạng có tổng = 5 thì mỗi số hạng đều <=5 

Step 2: Xây dựng tổng quát liệu có tồn tại dãy số có kết quả tổng là từ 0-->S
    Ví dụ:
        S-rng[0] = 5-2=3. Lấy 3 kiểm tra trong rng có tồn tại số 3 hay không?
        Giả sử tại vị trí rng[1] != 3 mà là rng[1] == 1 ==> ????
            
"""
pa = [0]*(S+1)
pa[0] = 1
hieu = [""]*(S+1)
print(pa)
for i in range(len(rng)):
    for j in range(S,rng[i]-1,-1):
        if pa[j]==0 and pa[j-rng[i]]==1:
            pa[j]=1
            hieu[j]=j- rng[i]
print(pa)
print(hieu)

if pa[S] !=1:
    print("Không tìm được kết quả")
else:
    result = []
    while S>0:
        result.append(S-hieu[S])
        S = hieu[S]
