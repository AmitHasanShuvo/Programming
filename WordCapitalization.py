'''

Author : kazi_amit_hasan
Problem: Word Capitalization

Solution: Just change the 0th word to uppercase from lowercase and print with the rest.
'''


string = input()
if (len(string) > 0 and string[0].islower()):
    print(string[0].upper() + string[1:])
else:
    print(string)
