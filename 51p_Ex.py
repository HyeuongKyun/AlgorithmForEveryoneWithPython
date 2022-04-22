
def fact(n):

    mul = 1
    if n == 0 :
            mul = 1
    elif n>0 :
        for i in range(1,n+1):
            mul = mul*i
    else :
        for i in range(1,-n+1):
            mul = mul*i*(-1)
    return mul
    
print(fact(0))
