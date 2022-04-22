

def fact_self(n):
    if n>0:
        while n<=1:
            return 1
        return n*fact_self(n-1)
    elif n==0:
        return 1
    else :
        m = abs(n)
        if m<=1:
            return 1
        return m*fact_self(m-1)*(-1)

print(fact_self(-5))