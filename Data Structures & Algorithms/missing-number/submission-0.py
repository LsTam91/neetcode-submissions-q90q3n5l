class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numset = set(nums)
        l = len(nums)
        for i in range(l):
            if i in numset:
                pass
            else:
                return i
        return l