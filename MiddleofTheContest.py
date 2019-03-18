'''

Author : kazi_amit_hasan
Problem: 1133A

'''

h1, m1 = map(int, input().split(':'))
h2, m2 = map(int, input().split(':'))

t1 = h1 * 60 + m1
t2 = h2 * 60 + m2

t3 = (t1 + t2) / 2

h = t3 // 60
m = t3 - h * 60

print("%02d:%02d" % (h, m))
