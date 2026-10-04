arr = []
n=int(input("Enter the total number of elements in the array : "))
print("Enter the elements of the array :")
for i in range(n):
    arr.append(int(input()))
count_even=0
count_odd=0
for i in range(n):
    if arr[i]%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("Even elements = ",count_even)
print("Odd elements = ",count_odd)