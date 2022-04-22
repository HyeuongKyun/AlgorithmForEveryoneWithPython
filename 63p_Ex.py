#유클리드 알고리즘

def gcd_u(a,b):
    m = max(a, b)
    n = min(a, b)
    if m%n == 0:
        return n
    else : 
        m = m%n
        
    return gcd_u(n,m)
    
    
print(gcd_u(5,3))