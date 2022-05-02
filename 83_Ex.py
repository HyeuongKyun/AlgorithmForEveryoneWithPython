# =============================================================================
# def search(list,num):
#     n = len(list)
#     result=[]
#     for i in range(n):
#         if list[i] == num:
#             result.append(i)
#     return result
# v=[17,92,18,33,58,7,33,42,17]
# 
# print(search(v,17))
# print(search(v,24))
# #계산 복잡도는 O(n)
# =============================================================================


def search_num(stu_no,stu_name,num):
    n=len(stu_no)
    
    for i in range(n):
        if stu_no[i] == num:
            return stu_name[i]
        
stu_no=[39,14,67,105]
stu_name=["Justion", "John", "Mike", "Summer"]

print(search_num(stu_no,stu_name,105))