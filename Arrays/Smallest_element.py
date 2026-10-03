arr = []
n=int(input("Enter the total number of elements in the array : "))
print("Enter the elements of the array :")
for i in range(n):
    arr.append(int(input()))
minimum=arr[0]
for i in range(1,len(arr)):
    if arr[i]<minimum:
        minimum=arr[i]
print("The minimum value is ",minimum)