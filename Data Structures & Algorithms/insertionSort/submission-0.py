# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        prev = 0
        res = []
        for i in range(0, len(pairs)):
            for j in range(1, i+1):
                if pairs[i-j+1].key<pairs[i-j].key:
                    pairs = pairs[:i-j] + [pairs[i-j+1]] + [pairs[i-j]] + pairs[i-j+2:]
            res.append(pairs)

        return res

