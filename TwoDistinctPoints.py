n = int(input())
for i in range(n):
    a, b, c, d = map(int, input().split(" "))
    if a != d:
        print(a, d)
    else:
        print(b, c)
