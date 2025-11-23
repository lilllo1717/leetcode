from collections import defaultdict
from collections import Counter

class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ToDo: Write Your Code Here.
        uniqueletter = Counter(ransomNote)
        uniquemag = Counter(magazine)
        
        for key, val in uniqueletter.items():
            if key not in uniquemag.keys() or uniquemag[key] < val:
                return False
        
        return True

from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = defaultdict(int)
        
        for char in magazine:
            char_count[char] += 1
        
        for char in ransomNote:
            if char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.canConstruct("hello", "hellworld"))  # Expected: true
    print(sol.canConstruct("notes", "stoned"))     # Expected: true
    print(sol.canConstruct("apple", "pale"))       # Expected: false