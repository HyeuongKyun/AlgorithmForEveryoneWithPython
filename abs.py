def abs_sign(a):
    if a < 0:
        return -a
    else :
        return a
    
import math
def abs_square(a):
    b = a*a
    return math.sqrt(b)

a = int(input('수 입력 :'))
print(abs_sign(a))
print(abs_square(a))