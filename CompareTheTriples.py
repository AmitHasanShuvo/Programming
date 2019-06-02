a = list(map(int, input().split()))
b = list(map(int, input().split()))

alice = sum([(1 if a[i] > b[i] else 0) for i in range
(3)])
bob = sum([(1 if a[i] < b[i] else 0) for i in range
(3)])

print(alice, bob)

# Another Solution:

a = list(map(int, input().split()))
b = list(map(int, input().split()))

alice = 0
bob = 0

for a_val, b_val in zip(a, b):
    if a_val < b_val:
        bob += 1
    elif a_val > b_val:
        alice += 1
print(alice, bob)
