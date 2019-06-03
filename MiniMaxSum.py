n = list(map(int, input().split(" ")))
a = sorted(n)
min = a[0] + a[1] + a[2] + a[3]
max = a[1] + a[2] + a[3] + a[4]

print(min, max)
