
def find_min_idx(lis):
    minx = min(lis)
    for i in range(len(lis)):
        if minx == lis[i]:
            return i 
    
def sel_sort(lis):
    graph=[]
    for i in range(len(lis)):
        graph.append(lis.pop(find_min_idx(lis)))
    return graph
        


li=[2,4,5,1,3,1]
print(sel_sort(li))