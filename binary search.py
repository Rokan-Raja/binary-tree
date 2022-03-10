def search(arr,low,high,x):
    if high > low:
        mid = (low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]< x:
            return search(arr,mid+1,high,x)
        else:
            return search(arr,low,mid-1,x)
        return -1
a=[]
n=int(input("Enter the Total Number:"))
for i in range(0,n):
    e=int(input("Enter the Element:"))
    a.append(e)
b=sorted(a)
print(b)
x=int(input("Enter the Searching Element:"))
c=search(b,0,len(b),x)
if c != -1:
    print("Element present in posision",str(c))
else:
    print("Element Not present in Array")

