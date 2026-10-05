arr=[2,-3,5,-1,4,-6]
left=0
right=0
while right<len(arr):
    if arr[right]<0:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
    right+=1
print(arr)