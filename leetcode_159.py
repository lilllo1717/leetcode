from collections import*

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        n = len(s)

        hash_map = defaultdict(int)
        max_len = 0
        left = 0
        for i, letter in enumerate(s):
            hash_map[letter] += 1
            while len(hash_map) > 2:
                left_char = s[left]
                hash_map[left_char] -= 1
                if hash_map[left_char] == 0:
                    del hash_map[left_char]
                left +=1
            max_len = max(max_len, i - left + 1)
        return max_len

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstringTwoDistinct("eceba"))