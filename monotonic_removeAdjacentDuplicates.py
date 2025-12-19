class Solution:
    def removeDuplicates(self, s: str) -> str:
        # TODO: Write your code here
        stack = []

        for letter in s:
            if stack and letter == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)

        return ''.join(stack)

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates("abccba")) # Output: ""
    print(solution.removeDuplicates("foobar")) # Output: "fbar"
    print(solution.removeDuplicates("abcd")) # Output: "abcd"