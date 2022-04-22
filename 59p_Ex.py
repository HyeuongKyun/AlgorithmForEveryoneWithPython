
# =============================================================================
# def sum_self(n):
#     while n<0:
#         return 0
#     return n + sum_self(n-1)
# 
# print(sum_self(4))
# =============================================================================



# 조금 까다로움 생각을 곰곰히 해봐야

list = [2,1,54,6,8]
def find_max_self(list):
        n = len(list)
        max = list[n-1]
        if n == 1:
            return list[0]
        elif max < list[n-2]:
            max = list[n-2]
            del list[n-1]
        else :
            list[n-2] = max
            del list[n-1]
        return find_max_self(list)
        
    
print(find_max_self(list))