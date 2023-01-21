"1. Nhập thư viện xlwings: thư viện giao tiếp Excel"
import xlwings as xw

"2. Đọc file Excel và gán vào biến wb"
wb = xw.Book(r"E:\py_Excel\File_Code\excel\tach_du_lieu.xlsx")
# print(wb)

"3. Gán biến shs chứa tất cả đối tượng Sheets trong Excel "
shs = wb.sheets
sh_data = shs('strResult')

"4. Gán biến rng chứa đối tượng range"
rng = sh_data.range("A5:Y42")

"5. Biến đổi rng thành list 2D: tức là lấy tất cả giá trị của rng"
data = rng.value
print(data)

"6. Viết hàm tách theo số nhóm cho trước: Trong bài là chia tổng số học sinh thành 4 tổ "
n_teams = 4
studtsOfTeam = len(data)//n_teams
studtsEndOfData = len(data)%n_teams

pth_Out = r"E:\\py_Excel\\File_Code\\Excel_Out\\"
for i in range(n_teams):
    team_export = []
    print(f'Team {i+1}')

    begin = i*studtsOfTeam
    after = begin + studtsOfTeam
    team_export.extend(data[begin:after])

    if i== n_teams-1 and studtsEndOfData !=0 :
        begin = after
        after = begin + studtsEndOfData
        team_export.extend(data[begin:after])
    # print(team_export)
    "7. Xuất dữ liệu tổ ra nhiều file Excel"
    file_Out = f'Team_{i+1}.xlsx'
    wb_new = xw.Book()
    wb_new.sheets[0].range("A1").value = team_export
    wb_new.save(pth_Out+file_Out)
    wb_new.close()
