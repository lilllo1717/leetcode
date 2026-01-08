class Solution:
    def stringShift(self, s, shift):
        n = len(s)
        for pair in shift:
            if pair[0] == 0:
                s = s[pair[1]%n:] + s[:pair[1]%n]
            elif pair[0] == 1:
                s = s[n - pair[1]%n :] + s[:n - pair[1]%n] 
        return(s)

if __name__ == "__main__":
    sol = Solution()
    print(sol.stringShift("abcdefg", [[1,1],[1,1],[0,2],[1,3]]))