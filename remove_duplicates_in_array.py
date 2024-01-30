# def remove_duplicates(arr):
#     unique_arr = []
#     for num in arr:
#         if num not in unique_arr:
#             unique_arr.append(num)
#     return unique_arr
def r(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i]!=arr[i+1]:
            print(arr[i],end=" ")
    print(arr[n-1],end=" ")
my_array = [1,2,3,4,4,4,4,4,4]
result = r(my_array)

