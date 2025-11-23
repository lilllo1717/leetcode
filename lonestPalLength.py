class Solution:
    def longestPalindrome(self, s: str) -> int:      
        length = 0
        # ToDo: Write Your Code Here. 
        letters = {}
        for let in s:
            if let not in letters:
                letters[let] = 1
            else:
                letters[let] += 1
        one_uneven = 0
        print(letters)
        for val in letters.values():
            if val%2 == 0:
                length+=val
            else:
                one_uneven = 1
                length += val - 1
        if one_uneven == 1:
            length+=1
                

        return length

sol = Solution()
print(sol.longestPalindrome("bananas"))   # Expected output: 5
print(sol.longestPalindrome("applepie"))  # Expected output: 5
print(sol.longestPalindrome("racecar"))   # Expected output: 7