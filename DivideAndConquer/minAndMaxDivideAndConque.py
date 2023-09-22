# Function Defination

def minAndmaxDandC(arr, lb, hb):
    if lb==hb:
        min = arr[lb]
        max = arr[lb]
    elif lb == hb-1:
        if arr[lb]>arr[hb]:
            min = arr[hb]
            max = arr[lb]
        else: 
            min = arr[lb]
            max = arr[hb]
    else:
        mid = lb + (hb - lb)//2
        minL, maxL = minAndmaxDandC(arr, lb, mid)
        minR, maxR = minAndmaxDandC(arr, mid+1, hb)

        if maxL > maxR:
            max = maxL
        else: 
            max = maxR

        if minL < minR:
            min = minL
        else: 
            min = minR
        
    return min, max 




# Driver Code

arr = [70, 50, 45, 10, 12, 15, 75, 29, 37, 57]
lb = 0
hb = len(arr)-1

result = minAndmaxDandC(arr, lb, hb)

print("Minimum and Maximum elements of given array are: ",result, "repectively")