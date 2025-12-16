arr=[52,34,23,14,56]
for i in arr:
    print(i,end=' ')
print()
print('--------reading along with index------------------------')
for i,x in enumerate(arr):
    print('index:',{i},'value:',{x})

print('----------reding with while loop----------------------')
# using whike
i=0
while i<len(arr):
    print(arr[i],end=',')
    i+=1

print()
print('---------reading with indices-----------------------')
print(arr[0:len(arr)-1])


print('---------reading in reveresed order-----------------')
for i in reversed(arr):
    print(i,end=',')

print()
print('---------reading with condition----------------------')
for i in arr:
    if i%2==0:
        print(i)

print()
print('---------reading with prefix sum')
prefix=0
for i in arr:
    prefix=prefix+i
    print(prefix,end=', ')
print()