class Solution:
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        i = 0
        n = len(A)
        for j in range(1, n):
            if A[j] != A[i]:
                i += 1
                A[i] = A[j]

        return i + 1
