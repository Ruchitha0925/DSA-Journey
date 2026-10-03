arr = []
n=int(input("Enter the total number of elements in the array : "))
print("Enter the elements of the array :")
for i in range(1,n):
    arr.append(int(input()))
maximum=arr[0]
for i in range(len(arr)):
    if arr[i]>maximum:
        maximum=arr[i]
print("The maximum value is ",maximum)