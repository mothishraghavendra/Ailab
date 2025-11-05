def countstring(s1,s2):
    if(len(s2)<len(s1)):
        return 0
    if(s2.startswith(s1)):
        return 1 + countstring(s1,s2[1:])
    else:
        return countstring(s1,s2[1:])

s1="ab"
s2="ababcab"
result=countstring(s1,s2)
print("The number of times the substring occurs is:",result)