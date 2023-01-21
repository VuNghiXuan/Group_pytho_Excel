
# func change strings into list strings
def get_list_str(strings:str)->list:
    return strings.split()

# Check for None in Excel
def chk_None(data)->True:    
    if isinstance(data, str):
        return True

'Covert strings into lower'
def covert_into_lower(strings:str)->str:
    return strings.lower()

# Compare recevide_data with dataset
def percent_compare(dataset:list, list_re_data:list)->float:
    result = [0,0]    
    per_max = 0    
    for data in dataset:
        if chk_None(data)==True:
            n_dataset = len(data.split())
            data_lower = covert_into_lower(data)

            per = 0
            for el_re_data in list_re_data:
                el_re_data_lower = covert_into_lower(el_re_data)
                if el_re_data_lower in data_lower:
                    per += 1/n_dataset

            if per>per_max:
                per_max = per
                result[0]= data
                result[1]= per_max
                
    return result

import xlwings as xw
book = xw.Book('E:\py_Excel\File_Code\excel\Danhsach.xlsx')
dataset = book.sheets('seach_str').range('A2:A37').value
recevide_data = book.sheets('seach_str').range('B2:B37').value


result =[]
for re_data in recevide_data:
    if chk_None(re_data)==True:
        re_data_lower = covert_into_lower(re_data)
        list_re_data = get_list_str(re_data_lower) #chuyển đổi thành list   
        result_i = percent_compare(dataset, list_re_data)
        
        result_i.insert(1, re_data)
        result.append(result_i)
        
"Write result in Excel"
book.sheets('seach_str').range('E2').value =  result     

        
        
        



