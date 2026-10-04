arr = []
n=int(input("Enter the total number of elements in the array : "))
print("Enter the elements of the array :")
for i in range(n):
    arr.append(int(input()))
max1=arr[0]
max2=float('-inf')
for i in range(1,len(arr)):
    if arr[i]>max1:
        max2=max1
        max1=arr[i]
    elif arr[i]<max1 and arr[i]>max2:
        max2=arr[i]
print("The second largest element is ",max2)