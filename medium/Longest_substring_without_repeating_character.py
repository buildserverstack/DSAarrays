### Interview Question: Longest Substring Without Repeating Characters

'''
You are given a string consisting of characters.
Your task is to find the **length of the longest substring** that contains **no repeating characters**.
A **substring** is a contiguous sequence of characters within the string.
---
### Rules
* All characters in the chosen substring must be **unique**
* Characters must appear **consecutively**
* You are not allowed to reorder characters
---
### Example
Input:
```
s = "abcabcbb"
```
Output:
```
3
```
Explanation:
The longest substring without repeating characters is `"abc"`.
---
### Additional Examples
* `"bbbbb"` → `1`
* `"pwwkew"` → `3` (substring `"wke"`)
---
### Constraints
* The string may contain letters, digits, symbols, and spaces
* The string can be empty
'''

# s = "abcabcbb"
s='a b c a'
# s="abababab"

def longest_substring_v1(s):
    max_str=0
    l=0
    r=0
    seen={}
    while r<len(s) and l<len(s):
        if s[r] not in seen:
            seen[s[r]]=1
            r+=1
            
        else:
            del seen[s[l]]
            l+=1
        if max_str<=len(seen)  :
            print(seen.keys())
            max_str=len(seen)
     
        
    print(max_str)
           
            

# longest_substring_v1(s)


def longest_substring_v2(s):
    seen={}
    left=0
    best=0
    for right,ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left=seen[ch]+1
        seen[ch]=right
        best= max(best,right-left+1)
    print(best)

longest_substring_v2(s)