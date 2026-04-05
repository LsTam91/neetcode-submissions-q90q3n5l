class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [char.lower() for char in s if char.isalnum()]
        n = len(string)
        if string[:n//2] == string[(n//2 + n%2):][::-1]:
            return True
        return False