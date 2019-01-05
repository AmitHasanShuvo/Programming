
'''

Author : Amit Hasan Shuvo
CodeChef ID : amithasan89
Problem: CHFINTRO (Chef and Interactive Contests
Solution: For each contestant, print a single line containing the string "Good boi" if this contestant does not forget to flush the output or "Bad boi" otherwise.


'''


A, B = map(int, input().split(' '))
for i in range(A):
    C = int(input())
    if C < B:
        print("Bad boi")
    else:
        print("Good boi")
