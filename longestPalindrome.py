class Solution1:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        n = len(s)

        for i in range(n):
            for j in range(n):
                if self.is_Pal(s, i, j) and (j - i + 1) >= max_len:
                    max_len = j - i + 1
                    start_index = i

        return s[start_index : start_index + max_len]

    def is_Pal(self, stri, i, j):
        while i < j:
            if stri[i] != stri[j]:
                return False
            i += 1
            j -= 1
        return True


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        n = len(s)
        start = 0

        for i in range(len(s)):
            len1 = self.is_Pal(s, i,i)
            len2 = self.is_Pal(s, i, i+1)
            current_max = max(len1, len2)
            if current_max > max_len:
                max_len = current_max
                start = i - (current_max - 1) // 2
        return s[start:start+max_len]
    def is_Pal(self, stri, left, right):
        while left >=0 and right <len(stri) and stri[left] == stri[right]:
            left-=1
            right+=1
        return right-left - 1

def main():
    sol = Solution2()
    strii = "babadaaaaa"
    print(sol.longestPalindrome(strii))
main()