arr = []
n=int(input("Enter the total number of elements in the array : "))
print("Enter the elements of the array :")
for i in range(n):
    arr.append(int(input()))
val=int(input("Enter the new element to be inserted : "))
index=int(input("Enter the index to insert the new element : "))
print("The original array is ",arr)
arr.append(None)
for i in range(len(arr)-1,index,-1):
    arr[i]=arr[i-1]
arr[index]=val
print("The updated array is ",arr)