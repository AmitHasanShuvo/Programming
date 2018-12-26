
'''

Author : Amit Hasan Shuvo
Codeforces ID : Kazi_Amit_Hasan
Problem: Codeforces 112A (Petya and Strings)
Solution: First you need to run a loop over any string length,convert the letters of each string in lowercase and compare them


'''

n = input().lower()
x = input().lower()

print(1 if n > x
      else -1
if x > n
else 0)
