class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:k], nums[k:] = nums[n - k:], nums[:n - k]
