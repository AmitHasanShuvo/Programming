class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:

        count = collections.Counter[A]
        for k in count:
            if count[k] > 1:
                return k
