from collections import Counter


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        occ = Counter(A)
        for k, v in occ.items():
            if v > 1:
                return k;
        return A[-1]
