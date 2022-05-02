def sel_sort(lis):
    n=len(lis)
    for i in range(n):
        for j in range(i,n):
            if lis[j] == min(lis[i:]):
                lis[i],lis[j] = lis[j],lis[i]
    return lis

li=[1,3,2,4,5,1,2,3]

print(sel_sort(li))
            
            