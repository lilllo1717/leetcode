class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0] == c: 
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        
        return ''.join(c * n for c, n in stack)  

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates("abbbaaca", 3))  # Output: "ca"
    print(solution.removeDuplicates("abbaccaa", 3))  # Output: "abbaccaa"
    print(solution.removeDuplicates("abbacccaa", 3))  # Output: "abbaa"