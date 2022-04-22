def solution(w,h):
    m = h/w
    if m == 1:
        return w*h-1*w
    elif m>1:
        if int(m)<m :
            return w*h-(int(m)+1)*w
        else: #int(m)=m
            return w*h-m*w
    else: #m<1
        return solution(h,w)
    
    
print(solution(5,7))













# =============================================================================
#https://programmers.co.kr/learn/courses/30/lessons/62048 
#import math as m
# 
# def solution(w,h):
#     return w*h - (w+h-m.gcd(w,h))
# =============================================================================
