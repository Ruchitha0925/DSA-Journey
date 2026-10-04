def pre_sum(arr,l,r):
    pre_arr=[0]
    for i in range(len(arr)):
        if i==0:
            pre_arr[i]+=arr[i]
        else:
            pre_arr.append(pre_arr[i-1]+arr[i])
    print("The sum of the values from index ",l," to ",r," is ",pre_arr[r]-pre_arr[l-1])
arr = []
n=int(input("Enter the total number of elements in the array : "))
print("Enter the elements of the array :")
for i in range(n):
    arr.append(int(input()))
l=int(input("Enter the beginning index : "))
r=int(input("Enter the ending index : "))
pre_sum(arr,l,r)