from collections import Counter

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return Counter(A).most_common()[0][0]