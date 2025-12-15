
class Solution:
    def isPalindromePossible(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:

                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindromePossible("racecar"))  # true
    print(solution.isPalindromePossible("abccdba"))  # true
    print(solution.isPalindromePossible("abcdef"))   # false