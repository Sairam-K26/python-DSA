#Done with Recursion
def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, 0, len(arr) - 1, x)
print(result)

#with loop

# def binary_search(arr, low, high, x):
#     while high >= low:

#         mid = (high + low) // 2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] > x:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1

# arr = [2, 3, 4, 10, 40]
# x = 100
# result = binary_search(arr, 0, len(arr) - 1, x)
# print(result)
