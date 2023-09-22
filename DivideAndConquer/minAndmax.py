# Function Defination

def minAndmax(arr):
    min = arr[0]
    max = arr[0]

    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        elif arr[i] > max:
            max = arr[i]
    
    return min, max





# Driver Code

arr = [70, 50, 45, 10, 12, 15, 75, 29, 37, 57]

result = minAndmax(arr)

print(result)

