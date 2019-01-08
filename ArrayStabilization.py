

'''

Author : kazi_amit_hasan
Problem: Array Stabilization

Solution: It is easy to see that we always have to remove either minimum or maximum of the array. So we can sort the array and the answer will be 𝑚𝑖𝑛(𝑎𝑛−1−𝑎1,𝑎𝑛−𝑎2). We also can do it without sort because two minimal and two maximal elements of the array can be found in linear time
'''


n = input()

s = list(map(int,input().split()))
s.sort()
print(min(s[-2] - s[0], s[-1] - s[1]))
