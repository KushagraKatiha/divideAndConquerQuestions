## Function Defination
def findTargetIndices(arr, target):
    idx_1 = 0
    idx_2 = 0
    for i in range(len(arr)-2):
        for j in range(i+1, len(arr)-1):
            if arr[i]+arr[j] == target:
                idx_1 = i
                idx_2 = j
    return idx_1,idx_2            


## Driver Code

arr = [20, 40, 50, 75, 120, 145, 200]
target = 90

result = findTargetIndices(arr, target)
print(result)