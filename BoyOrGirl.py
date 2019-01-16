
'''

Author : kazi_amit_hasan
Problem: Boy or Girl

Solution: Count the lenght and if it's even then its girl other wise it's a boy
'''


n = input()
s = len(set(n))
if s % 2 ==0 :
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
