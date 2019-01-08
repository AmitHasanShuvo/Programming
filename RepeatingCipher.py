



'''

Author : kazi_amit_hasan
Problem: Repeating Cipher

Solution: Very easy problem. 
'''
n = int(input())
s = input()
ans = s[0]
i = 1
j = 1

while (j < len(s)):
    ans = ans + s[j]
    i = i + 1
    j = j + i
print(ans)
