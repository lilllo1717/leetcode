class Solution:
    def rotateString(self, s, goal):
        
        # n = len(s)
        # for move in range(0, len(s)):
        #     s = s[n-1:] + s[:n-1]
        #     if s == goal:
        #         return True
        # return False
        if len(s) != len(goal):
            return False
        return goal in s+s

if __name__ == '__main__':
    sol = Solution()
    print(sol.rotateString( "abcde", "cdeab"))