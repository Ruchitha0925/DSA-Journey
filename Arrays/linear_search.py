arr = []
n=int(input("Enter the total number of elements in the array : "))
print("Enter the elements of the array :")
for i in range(n):
    arr.append(int(input()))
key=int(input("Enter the element to be found : "))
found=0
for i in range(n):
    if arr[i]==key:
        print("Element found at the index ",i)
        found=1
        break
if(found==0):
    print("Element not Found")