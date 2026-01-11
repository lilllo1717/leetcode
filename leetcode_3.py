class Solution:
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        hash_map = {}
        left = 0

        for i in range(len(s)):
            if s[i] in hash_map and hash_map[s[i]] >= left:
                left = hash_map[s[i]] + 1

            hash_map[s[i]] = i

            max_len = max(max_len, i - left + 1)

        return max_len

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))