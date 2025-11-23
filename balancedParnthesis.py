class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:

                if not stack:
                    return False

                top = stack.pop()

                if c == ')' and top != '(':
                    return False
                if c == '}' and top != '{':
                    return False
                if c == ']' and top != '[':
                    return False
        return not stack


sol = Solution()
test1 = "{[()]}"; # Should be valid
test2 = "{[}]";   # Should be invalid
test3 = "(]";     # Should be invalid

print("Test 1:", sol.isValid(test1))
print("Test 2:", sol.isValid(test2))
print("Test 3:", sol.isValid(test3))