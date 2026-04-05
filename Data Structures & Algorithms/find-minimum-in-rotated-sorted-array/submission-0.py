class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif nums[:n//2][-1] < nums[n//2:][-1]:
            return self.findMin(nums[:n//2])
        else:
            return self.findMin(nums[n//2:])