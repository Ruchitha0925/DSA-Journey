arr = []
n=int(input("Enter the total number of elements in the array : "))
print("Enter the elements of the array :")
for i in range(n):
    arr.append(int(input()))
print("The original array is ",arr)
pos=0
for i in range(n):
    if arr[i]!=0:
        arr[pos]=arr[i]
        pos+=1
while(pos<n):
    arr[pos]=0
    pos+=1
print("The final array is ",arr)