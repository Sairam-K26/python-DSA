arr=[0,1,2,0,1,2,1,2,0]
# arr=[2,2,2,1,1,1,0,0,0]
n=len(arr)
low=0
high=n-1

for i in range(n):
    if i<=high :
        if arr[i]==0:
            
            arr[i],arr[low]=arr[low],arr[i]
            
            low+=1
        elif arr[i]==2:
            
            arr[i],arr[high]=arr[high],arr[i]
 
            high-=1    
        else:
            i+=1
                
print("Sorted array is",arr)

           
