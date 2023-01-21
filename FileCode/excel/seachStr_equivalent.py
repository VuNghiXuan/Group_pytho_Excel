# func change strings into list strings
def get_list_str(strings:str)->list:
    return strings.split()

'Covert strings into lower'
def covert_into_lower(strings:str)->str:
    return strings.lower()

# Compare recevide_data with dataset
def percent_compare(dataset:list, list_re_data:list)->float:
    result = [0,0]
    per_max = 0    
    for data in dataset:
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

dataset = ['Nguyễn Thị Thu Nhi', 'Lê Tấn Tài', 'Hồ Quang Nhi Đại']
recevide_data = ['NGUYỄN THU NHI', 'tẤN TÀI']


result =[]
for re_data in recevide_data:
    re_data_lower = covert_into_lower(re_data)
    list_re_data = get_list_str(re_data_lower) #chuyển đổi thành list   
    result_i = percent_compare(dataset, list_re_data)
    
    result_i.insert(1, re_data)
    result.append(result_i)
    
print(result)
        
        
        
        



