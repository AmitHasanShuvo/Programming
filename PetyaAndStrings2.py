
'''

Author : Amit Hasan Shuvo
Codeforces ID : Kazi_Amit_Hasan
Problem: Codeforces 112A (Petya and Strings)
Solution: First you need to run a loop over any string length,convert the letters of each string in lowercase and compare them


'''

def compare(str1, str2):
    for i in range(0, len(str1)):
        if (str1.lower()[i] < str2.lower()[i]):
            return -1
        elif (str1.lower()[i] > str2.lower()[i]):
            return 1
    return 0


if __name__ == "__main__":
    str1 = input()
    str2 = input()

    print(compare(str1, str2))
