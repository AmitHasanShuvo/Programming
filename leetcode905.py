class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return ([x for x in A if x%2==0 ]+[x for x in A if x%2==1 ])
