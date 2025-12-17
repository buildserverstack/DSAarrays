s='conversation'
t='voices rant on'
words={}
def is_anagaram(s,t):
    if len(s)!=len(t):
        return False
    seen={}
    for ch in s:
        seen[ch]=seen.get(ch,0)+1
    for ch in t:
        if ch not in seen or seen[ch]==0:
            return False
    return True

            
print(is_anagaram(s,t))
# not case sensitive
# doesnt ignore spaces
# doesnt ignore special characters



