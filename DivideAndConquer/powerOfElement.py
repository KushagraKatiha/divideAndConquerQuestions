# funtion defination
def powOfEle(a, n):
    pow = 1
    for i in range(1, n+1):
        pow = pow*a

    return pow

# Driver Code 

a = 2
n = 10

output = powOfEle(a, n)
print(output)