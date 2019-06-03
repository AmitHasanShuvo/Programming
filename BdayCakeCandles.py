n = input()
t = list(map(int, input().split(" ")))
a = sorted(t)

print(a.count(max(a)))
