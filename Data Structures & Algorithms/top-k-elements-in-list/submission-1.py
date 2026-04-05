class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        vals = {}
        for n in nums:
            if str(n) in vals:
                vals[str(n)] += 1
            else:
                 vals[str(n)] = 1
        res=[]
        for i in range(k):
            res.append(max(vals, key=vals.get))
            vals[res[-1]] = -1

        return res