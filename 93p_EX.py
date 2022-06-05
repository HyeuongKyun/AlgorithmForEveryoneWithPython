#list 안에서 삽입 정렬을 하는 방법 (새로운 리스트를 만들지 않고)
def ins_sort(list):
    n=len(list)
    for i in range(1,n):
        comp=list[i];
        j=i-1;
        while j >= 0 and  list[j] > comp: #0보다 크다는 조건을 안달아주면 리스트의 -1은 오른쪽에서부터 카운트 되기 때문에 막아줘야함
            list[j+1] = list[j]; #위 조건이 만족된다는건 이동이 무조건 발생한다는 뜻, comp를 넣을 공간 확보하기 위해 한칸씩 이동 
            j -= 1;
        list[j+1]=comp; #+1 해줘야 하는 이유는 while문 안에서 -1 한 상태로 나오기 때문에 원하는 j를 찾기 위해서는 +1를 해주어야한다.
    return list;
        
list = [3 , 2 , 1];
        
print(ins_sort(list));