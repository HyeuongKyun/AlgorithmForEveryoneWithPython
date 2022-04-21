#set(집합)은 list에서 append는 add() 집합은 index 개념이 없고 중복해서 들어가지 않는다.
#set에서 자주 쓰는 기능 s=set(); len(s), s.add(x), s.clear(), x in s

list = ['a', 'b', 'c', 'a', 'c', 'd', 'd']


def find_same_name(list):
    s = set() 
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                s.add(list[i])
                break
    return s
                
print(find_same_name(list))