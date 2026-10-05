arr=[1,1,2,2,3,4,4]
unique=0
for i in range(1,len(arr)):
    if arr[unique]!=arr[i]:
        unique+=1
        arr[unique]=arr[i]
print(arr[:unique + 1])