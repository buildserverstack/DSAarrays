num1=[1,2,3,0,0,0]
num2=[2,5,6]
n=3
m=3

def mergesortedarray(num1,n,num2,m):
    i=n-1
    j=m-1
    k=m+n-1
    while i>=0 and j>=0:
        if num1[i] >= num2[j]:
            num1[k]=num1[i]
            i-=1
        else:
            num1[k]=num2[j]
            j-=1
        k-=1
    # copying remaining elements of j
    while j>=0:
        num1[k]=num2[j]
        j=-1
        k-=1

    return num1


print(mergesortedarray(num1,n,num2,m))