

#This is not correct solution
n = int(input())
for i in range(n):
    l, r, d = int(input().split())
    p = int (l) + int (r)
    if p % d == 0:
        print(p)
