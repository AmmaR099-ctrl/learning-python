# function that filters data below threwshold
def filter_data(d_list,value):
    data_list=[]
    for i in d_list:
        if i>=value:
            data_list.append(i)
    return data_list

# function that divide the filtered data with max value
def division(data_list):
    m=data_list[0]
    for i in data_list:
        if i>m:
            m=i
    final_list=[]
    for i in data_list:
        i=i/m
        final_list.append(i)
    return final_list

# input data in list and threwshold value
n=int(input("enter number of values in data: "))
data_list=[]
for i in range (n):
    data_list.append(int(input(f"enter {i+1} value: ")))
threwshold=int(input("enter the threwshold value: "))
filtered_list= filter_data(data_list,threwshold)
result=division(filtered_list)
print(result)
