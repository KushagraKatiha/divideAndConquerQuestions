## Function Defination
def findTargetIndices(arr, target):
    l = 0
    h = len(arr)-1
    for i in range(len(arr)-1):
        if arr[l]+arr[h] == target:
            return l, h
        elif arr[l]+arr[h] > target:
            h = h-1
        else:
            l+=1

    return -1, -1


## Driver Code
arr = [20, 40, 50, 75, 120, 145, 200]
target = 90

result = findTargetIndices(arr, target)
print(result)