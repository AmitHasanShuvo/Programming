'''

Author : Amit Hasan Shuvo
Codeforces ID : Kazi_Amit_Hasan
Problem: Codeforces 4A (WaterMelon)
Solution: Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.


'''


class Watemelon:
    def solve(self, w):
        if (w < 2):
            return "NO"
        elif ((w - 2) % 2 == 0):
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    w = int(input())
    wl = Watemelon()
    print(wl.solve(w))
