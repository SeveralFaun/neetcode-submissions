class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')':'(', '}':'{', ']':'[' }
        for i in range(len(s)):
            if s[i] in close_to_open:
                if stack and stack[-1] == close_to_open[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if not stack else False
