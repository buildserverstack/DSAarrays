### Interview Question: Move Zeroes

'''
You are given an integer array.
Your task is to **move all the zeroes to the end of the array**, while **maintaining the relative order of the non-zero elements**.
---
### Rules
* The operation must be done **in-place**
* Do **not** create a new array
* The relative order of non-zero elements must remain the same
---
### Example
Input:
```
nums = [0, 1, 0, 3, 12]
```
Output:
```
[1, 3, 12, 0, 0]
```
---
### Constraints
* Array may contain negative numbers
* Array length can be zero
* You must use **O(1)** extra space
---

### Follow-up Questions (Common in Interviews)
* How do you minimize the number of writes?
* What happens if the array contains no zeroes?
* What if all elements are zero?
---
'''
# nums = [0, 1, 0, 3, 12]
nums = [5, 4, 3, 2, 1, 0, 0]


def move_zeros(nums):
    pos=0
    for i in nums:
        if i!=0:
            nums[pos]=i
            pos+=1

    rem=len(nums)-pos
    for i in range(pos,len(nums)):
        nums[i]=0

    print(nums)
          

            
            
            

         

    
move_zeros(nums)
