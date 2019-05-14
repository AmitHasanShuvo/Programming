class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x * x for x in A)
