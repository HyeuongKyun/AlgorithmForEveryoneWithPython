def gcd(a,b):
    m=min(a,b)
    
    while a%m!=0 or b%m!=0:
        m = m-1
        
    return m
        
        
        
print(gcd(24,16))