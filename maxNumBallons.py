from collections import defaultdict
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        min_count = float('inf')
        freq = Counter(text)
        need = Counter('balloon')
        for c in need:
            least = freq[c] // need[c]
            if least < min_count:
                min_count = least
        # ToDo: Write Your Code Here.
        return min_count
