from collections import defaultdict

class Solution1:
    def largestUniqueNumber(self, A: List[int]) -> int:
        maxUnique = -1
        unique = {}
        for num in A:
            unique[num] = unique.get(num, 0) + 1
        for key, val in unique.items():
            if val == 1:
                new_max = key
                if new_max > maxUnique:
                    maxUnique = new_max
        # ToDo: Write Your Code Here.
        return maxUnique

from collections import defaultdict
from typing import List

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        freq = defaultdict(int)
        
        for num in A:
            freq[num] += 1
        
        maxUnique = -1
        for key, value in freq.items():
            if value == 1:
                maxUnique = max(maxUnique, key)
        
        return maxUnique

if __name__ == "__main__":
    sol = Solution()
    print(sol.largestUniqueNumber([5, 7, 3, 7, 5, 8]))  # Expected: 8
    print(sol.largestUniqueNumber([1, 2, 3, 2, 1, 4, 4]))  # Expected: 3
    print(sol.largestUniqueNumber([9, 9, 8, 8, 7, 7]))   # Expected: -1
