list=[2,4,5,1,3]

def sel_sort(list):
    for i in range(len(list)-1):
        min_index = i;
        for j in range(i+1,len(list)):
            if list[min_index] > list[j]:
                min_index = j;
        list[i],list[min_index] = list[min_index],list[i];
    
    return list

print(sel_sort(list))