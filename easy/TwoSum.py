# given an array nums and a target , return indices of two numbers that add up to the target

nums=[5,2,3,4,5,6,7]
target=7
hm={}
def two_sum(nums,target):
    for i,x in enumerate(nums):
        if target-x in hm:
            return [nums[hm[target-x]],nums[i]]
        else:
            hm[x]=i


    
print(two_sum(nums,target=target))

# print(hm)