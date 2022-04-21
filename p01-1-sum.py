def sum_1(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s

a=int(input('n을 입력해주세요. : '))

print(sum_1(a))


def sum_2(n):
    return n*(n+1)//2   # / 하나만 하면 float으로 나오게 되고 //로 하게되면 정수 나눗셈으로 된다.

b=int(input('다른 n을 입력해 보세요. :'))

print(sum_2(b))


#두가지 fun 중에 어떤 방법이 더 좋은 것인지 판단할 때 필요한 것이 '알고리즘 분석'
#작성만큼 분석도 중요하다. 수학 이론이 필요한 경우가 많다.
#입력의 크기가 sum_1에는 수행 성능에 있어서 영향을 많이 미치고 sum_2는 입력 크기에 영향을 받지않는다.
#sum_1은 덧셈 n번, sum_2는 덧셈,곱셈,나눗셈 각 1번씩(총 3번)

#계산이 얼마나 복잡한지 나타낸 정도를 '계산 복잡도(complexity)'라고 한다.
#계산 복잡도를 표현하는 방법은 많지만 그 중 대문자(O)를 많이 사용한다.

#대문자 O 표기법
#O(n) : 계산 횟수가 입력 크기 n과 비례할 때 (O(3n)이런식으로 하지 않음 그냥 선형인지 아닌지)
#O(1) : 계산 횟수가 입력 크기 n과 무관할 때 (O(1)과 같이 표시해줌 sum_2 같은 경우)

#계산 복잡도는 시간 복잡도와 공간 복잡도(space complexity)로 나뉜다.
#공간 복잡도는 얼마나 많은 공간(메모리/기억장소)이 필요한지 분석한 것이다.
#보통 그냥 계산 복잡도라고 하면 공간 복잡도를 언급하는 경우가 많다고 합니다.

