class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        n = len(A)
        count = 1
        for i in range(1, n):
            count = count + 1 if A[i] == A[i - 1] else 1
            if count == n / 2:
                return A[i]
        return A[-1]
