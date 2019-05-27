class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                return i
