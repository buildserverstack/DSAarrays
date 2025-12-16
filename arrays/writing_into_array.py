# append into array
arr=[1,2,3]
arr1=[]
arr1.append(arr)
print(arr1)
arr2=[[0]*3 for _ in range(3)]
print(arr2)

# inserting into array
arr3=[10,20,30,40]
arr3.insert(1,15)
print(arr3)


# extend the array
arr4=[3]
arr4.extend([4,5,6])
print(arr4)

# overwrite
arr5=[2,2,3]
arr5[0]=1
print(arr5)



# list comprehension
arr6=[i*i for i in range(5)]
print(arr6)


