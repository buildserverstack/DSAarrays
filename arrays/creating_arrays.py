from array import array


arr=[1,2,3,4,5]
print(arr)
arr1=[0]*10
print(arr1)
print(len(arr1)) 
arr2=[None]*10
print(arr2)


# append
arr3=[1]
arr3.append(arr2)
print(arr3)

arr4=['wow']
arr4.append(arr4)
print(arr4)

arr5=[[0]*3 for _ in range(3)]
print(arr5)


arr6=array('f',[1,2,3,4,5])
print(arr6)