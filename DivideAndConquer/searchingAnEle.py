## Function Defination

def findEle(arr, n):
    index = 0
    for i in range(len(arr)-1):
        if arr[i] == n:
            index = i
    return index        

## Driver Code

arr = [2, 4, 8, 12, 20, 25, 50, 70]
n = 50 
result = findEle(arr, n)
print(result)