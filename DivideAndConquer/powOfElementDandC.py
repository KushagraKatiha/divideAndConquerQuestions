from fractions import Fraction

## Function Defination

def findPow(a, n):
    if n == 0:
        return 1
    elif n == 1:
        return a 
    else:
        if n < 0:
            m = n*-1
            mid = m // 2
            b = findPow(a, mid)
            result = b*b
        else:
            mid = n // 2
            b = findPow(a, mid)
            result = b*b
    

        if n < 0:
            if n % 2 == 0 :
                return Fraction(1, result)
            else: 
                return Fraction(1,(result * a))
        
        if n % 2 == 0 :
            return result
        else: 
            return result * a


## Driver Code

a = 2
n = 10

result = findPow(a, n)
print(result)