

'''

Author : kazi_amit_hasan
Problem: ChatRoom

Solution: Just search for hello word that exists in any places.
'''


import re

n = input()
if re.search("h.*e.*l.*l.*o",n):
    print("YES")


else:
    print("NO")
