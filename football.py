'''

Author : kazi_amit_hasan
Problem: Football

Solution: Just search for seven zero or ones in a row.
'''

s = input()

if '1'*7 in s or '0'*7 in s:
    print("YES")
else:
    print("NO")