class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(n+1):
            bits = i
            while bits!=0:
                res[i] += 1
                bits = bits & (bits - 1)
        return res
