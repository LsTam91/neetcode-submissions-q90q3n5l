class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + ' ' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        while s:
            u = int(s.split(' ')[0])
            ind = len(str(u)) + 1
            decoded.append(s[ind:u + ind])
            s = s[ind + u:]
        return decoded