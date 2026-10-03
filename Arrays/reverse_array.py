arr = []
n=int(input("Enter the total number of elements in the array : "))
print("Enter the elements of the array :")
for i in range(n):
    arr.append(int(input()))
new_arr=[]
for i in range(len(arr)-1,-1,-1):
    new_arr.append(arr[i])
print("The original array is ",arr)
print("The array after reversal is ",new_arr)