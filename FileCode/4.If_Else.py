"""
Từ khóa (if, elif, else)	Kiểm tra điều kiện	:	Thực hiện điều kiện
Nếu  (if)	Excel	thì	Lương 10 triệu
Ngược lại nếu (elif)	Excel và VBA		Lương 15 triệu
Ngược lại nếu (elif)	Excel và Python		Lương 20 triệu
Ngược lại (else)			Không được tuyển dụng

"""
dk_toi_thieu = "Excel"
dk_kynang = "Python"

if dk_toi_thieu == "Excel" and dk_kynang == "VBA": 
    print("Lương 15 triệu")
elif dk_toi_thieu == "Excel" and dk_kynang == "Python": 
    print("Lương 20 triệu")
elif dk_toi_thieu == "Excel": 
    print("Lương 10 triệu") 
    # print("Lương tháng 13 là: 20 triệu") 
else:
    print("Không được tuyển dụng")

         