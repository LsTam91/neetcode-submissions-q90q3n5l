class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []
        for i, el in enumerate(s):
            if el in brackets:
                stack.append(brackets[el])
            else:
                if stack and el == stack[-1]:
                    stack.pop()
                else:
                    return False
        return stack==[]