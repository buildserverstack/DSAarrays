'''
**Problem: Maximum Subarray (Kadane’s Algorithm)**
You are given an integer array `nums` of length `n`, which may contain both positive and negative numbers.
Your task is to find the **contiguous subarray (containing at least one element)** that has the **maximum possible sum**, and return that sum.
---
**Constraints**
* The subarray must be contiguous.
* The subarray must contain at least one element.
* The array can include negative numbers, zeros, and positive numbers.
---
**Example**
* Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
* Output: `6`
* Explanation: The contiguous subarray `[4, -1, 2, 1]` has the largest sum.
---
**Clarifications (as in an interview)**
* You are expected to solve this in **linear time**.
* Avoid brute-force approaches that check all subarrays.
* Think in terms of:
  * When it is beneficial to **extend** a subarray.
  * When it is better to **start fresh** from the current element.
---
**Follow-up Questions an Interviewer May Ask**
1. What happens if **all numbers are negative**?
2. Why does a greedy approach work here?
3. Can you explain your logic using a **running sum** concept?
4. How would you modify the solution to also return the **start and end indices** of the subarray?
If you want, I can next:
* Give **all edge cases** (no code), or
* Ask you to **walk through your reasoning step by step** like a real interview.
'''

from math import inf


input=[-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maximum_subarray(input):
    bag=0
    best=-inf
    start=0
    end=0
    for i,val in enumerate(input):
        if bag+val>=bag:
            bag=bag+val
            start+=1
        else:
            end=i
        
        if best<bag:
            start=i

        


            

    print(best)
    print(f"start={start} end={end}")

maximum_subarray(input)