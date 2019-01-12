'''
Problem: Team forming conetest for BUET ICPC

Status: AC :D

'''


a, b = map(int,input().split())
x = int(a / b)
y = int(a % b)
z = (a / b)

print(x, y, '{0:4f}'.format(z))
