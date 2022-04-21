


# =============================================================================
# def find_max(a):
#     max = a[0]
#     for i in range(1,len(a)):
#         if max < a[i]:
#             max = a[i]
#     return max
# 
# 
# 
# a = [1,2,45,6,7,8,54,51,5,6,13,12]
# 
# print(find_max(a))
# 
# 
# #38p 최댓값의 위치(인덱스)를 구하는 알고리즘
# 
# 
# def find_max_index(a):
#     max = a[0]
#     index = 0
#     for i in range(1,len(a)):
#         if max < a[i]:
#             max = a[i]
#             index = i
#     return index
# 
# print(find_max_index(a))
# =============================================================================


# 숫자 n개를 리스트로 입력받아 최솟값을 구하는 프로그램 만들기

# =============================================================================
# def find_min(a):
#     min = a[0]
#     for i in range(1,len(a)):
#         if min > a[i]:
#             min = a[i]
#     return min
# 
# a = list(map(int,input('리스트에 들어갈 숫자들을 입력해주세요. : ').split()))
# 
# print(find_min(a))
# =============================================================================



#map을 사용하지 않고 입력 받아서 최솟값을 구하는 방
def find_min(a):
    min = a[0]
    for i in range(1,len(a)):
        if min > a[i]:
            min = a[i]
    return min



num = int(input('리스트의 길이를 정해주세요. :'))
list = []

for i in range(num):
    s = int(input('수를 입력하세요. :'))
    list.append(s)
    
print(find_min(list))












