class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        # ToDO: Write Your Code Here.
        balance, counter = 0, 0
        for char in S:
            balance += 1 if char == '(' else -1
            if balance == -1:
                counter += 1
                balance += 1
        return counter + balance

if __name__ == "__main__":
    solution = Solution()
    print(solution.minAddToMakeValid("(()"))        # Example 1
    print(solution.minAddToMakeValid("))(("))       # Example 2
    print(solution.minAddToMakeValid("(()())("))    # Example 3