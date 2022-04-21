

def squaresum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum
    

num1 = int(input('n을 입력하세요. : '))

print(squaresum(num1))

#계산 복잡도는 n에 따라 정비례하게 들어나므로 O(n)

def squaresumD(n):
    return n*(n+1)*(2*n+1)//6

num2 = int(input('n을 입력하세요 : '))

print(squaresumD(num2))

#계산 복잡도는 O(1), 입력 크기에 상관없이 계산복잡도가 바뀌지 않기 때문이다.

