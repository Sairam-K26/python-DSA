# def max_ind(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#     return (j)
#     # return (arr)
# print(max_ind([1,4,7,2,8]))

def max_ele(arr):
    ind= 0
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] >= max_element:
            max_element = arr[i]
            ind = i
    return ind

lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	lst.append(ele) 
     
print("index_of_Max_element is :",max_ele(lst))



