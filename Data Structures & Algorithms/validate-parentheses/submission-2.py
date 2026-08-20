class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        other = {'[':']',
        '{': '}', '(':')'}

        for c in s:
            if len(stack)==0:
                stack.append(c)
            else:
                if stack[-1] in other and other[stack[-1]] == c:
                    stack.pop()
                else:
                    stack.append(c)
        
        return len(stack)==0
        