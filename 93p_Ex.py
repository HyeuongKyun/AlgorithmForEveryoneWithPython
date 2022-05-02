def find_ins_idx(lis,value):
    for i in range(len(lis)):
        if value < lis[i]:
            return i
    return len(lis)
    

def ins_sort(lis):
    graph=[]
    while lis:
        value=lis.pop(0)
        graph.insert(find_ins_idx(graph, value), value)
    
    return graph

d=[2,4,5,1,3]
print(ins_sort(d))