# def binary_search(arr, target, left, right):
#     while left <= right:
#         mid = left + (right - left) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# def find_target_sum(arr, target):
#     # Sort the array if it's not already sorted
#     arr.sort()

#     for i in range(len(arr)):
#         complement = target - arr[i]
#         index = binary_search(arr, complement, i + 1, len(arr) - 1)
#         if index != -1:
#             return [arr[i], arr[index]]

#     return None

# # Example usage
# arr = [1, 2, 3, 4, 5, 6, 7]
# target = 10
# result = find_target_sum(arr, target)

# if result:
#     print(f"Pair with target sum {target} found: {result[0]} and {result[1]}")
# else:
#     print(f"No pair found with target sum {target}")


## Function Defination
# Binary Search

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