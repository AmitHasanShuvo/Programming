class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).count('1')
