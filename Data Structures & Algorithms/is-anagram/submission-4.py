class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n == len(t):
            s_set, t_set = {}, {}
            for i in range(n):
                if not s[i] in s_set:
                    s_set[s[i]] = 1
                else:
                    s_set[s[i]] += 1
                if not t[i] in t_set:
                    t_set[t[i]] = 1
                else:
                    t_set[t[i]] += 1
            if s_set == t_set:
                return True
        return False
