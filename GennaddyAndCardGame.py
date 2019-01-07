'''

Author : kazi_amit_hasan
Problem: Hello 2019,Problem A

Solution: Just check that first input is present in next input or not
'''


t= input()
h = input()

if t[0] in h or t[1] in h:
    print("YES")
else:
    print("NO")
