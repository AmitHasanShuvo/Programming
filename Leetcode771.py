class Solution:

    def numJewelsInStones(self, J, S):
        counter = 0
        for stones in S:
            if stones in J:
                counter = counter + 1
        return counter
