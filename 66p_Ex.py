##아직 안끝

def pibo(n):
    list = [0, 1]
    if len(list) != n:
        m=len(list)
        list.append(list[m-1]+list[m-2])
        return pibo(n-1)
    else :
        return list[len(list)-1]
print(pibo(5))



# list = [1,2,3]
# print(list[-1], list[-2], list[-3] )