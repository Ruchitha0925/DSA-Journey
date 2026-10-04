seen={}
arr = []
n=int(input("Enter the total number of elements in the array : "))
print("Enter the elements of the array :")
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    if arr[i] in seen:
        print("Duplicate element is ",arr[i])
    else:
        seen[arr[i]]=1
