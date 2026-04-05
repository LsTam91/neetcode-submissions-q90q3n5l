class Solution:
    def anagrams(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            return sorted(s) == sorted(t)
        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        res = [[strs[0]]]
        for i in range(1, n):
            nogroup = True
            for group in res:
                if self.anagrams(group[0], strs[i]):
                    group.append(strs[i])
                    nogroup = False
                    break
            if nogroup:
                res.append([strs[i]])

        return res
            

