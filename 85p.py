list = [2 , 4 , 5 , 1, 3];


def find_min_index(list):
    min_index = 0;
    for i in range(1,len(list)) :
        if list[i] <list[min_index]:
            min_index = i;
    return min_index;
            
        

def sel_sort(list) :
    min_index = 0;
    sort=[];
    
    while list:
        min_index = find_min_index(list);
        sort.append(list[min_index]);
        list.pop(min_index);
    return sort;

print(sel_sort(list));
    