def binarySearch(arr, target, lb, hb):
    while lb <= hb:
        mid = lb + (hb-lb)//2
        if arr[mid] > target:
            hb = mid-1
        elif arr[mid] < target:
            lb = mid+1
        else:
            return mid
    return -1


def findSum(arr, target):
    for i in range(len(arr)):
        x = target - arr[i]
        index = binarySearch(arr, x, i+1, len(arr)-1)
        if index != -1:
            return [i, index]
    
    return None

## Driver Code
arr = [20, 40, 50, 75, 120, 145, 200]
target = 115

result = findSum(arr, target)

if result:
    print(f"Indices are {result[0]} and {result[1]}")
else:
    print(f"Not Found !!")