v=[17,92,18,33,58,7,33,42]

def search(list,num):
    n = len(list)
    for i in range(n):
        if list[i] == num:
            return i
    return -1
        
print(search(v,18))
print(search(v,33))
print(search(v,900))