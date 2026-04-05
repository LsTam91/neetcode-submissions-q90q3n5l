class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        size = len(nums)
        res = []
        for i in range(size):
            target = - sorted_nums[i]
            if target < 0:
                break

            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            j, k = i+1, size-1
            while j<k:
                if target < sorted_nums[j] + sorted_nums[k]:
                    k-=1
                elif target > sorted_nums[j] + sorted_nums[k]:
                    j+=1
                else:
                    res.append([sorted_nums[i], sorted_nums[j], sorted_nums[k]])
                    k-=1
                    j+=1
                    while sorted_nums[j]==sorted_nums[j-1] and j<k:
                        j+=1
        return res
        