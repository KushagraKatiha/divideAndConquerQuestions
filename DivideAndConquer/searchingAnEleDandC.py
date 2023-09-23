## Function Defination
def findEleDandC(arr, n, lb, hb):
    if lb == hb:
        if arr[hb] == n:
            return hb
        else:
            return "Element not present in Array"
    else:
        mid = lb + (hb-lb)//2
        if arr[mid] < n:
            index = findEleDandC(arr, n , mid+1, hb)
        else:
            index = findEleDandC(arr, n , lb, mid)

        return index


## Driver Code

arr = [2, 4, 8, 12, 20, 25, 50, 70]
n = 8
lb = 0
hb = len(arr)-1

result = findEleDandC(arr, n, lb, hb)
print(result)