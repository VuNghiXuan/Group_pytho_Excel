import xlwings as xw
def remove_chart(obj_sh):
    for obj in obj_sh.shapes:
        print(obj)
        obj.delete()

wb = xw.Book(r"E:\py_Excel\QA\excel\chart.xlsx")
sh_chart = wb.sheets[0]
data = sh_chart.range("A2:I7")

"Xóa obj chart"
remove_chart(sh_chart)

chart = sh_chart.charts.add()
chart.set_source_data(data)

chart.chart_type = 'pie'
