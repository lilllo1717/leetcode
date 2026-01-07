from heapq import *
from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        count_words = Counter(words)
        max_heap = []
        
        for key, val in count_words.items():
            heappush(max_heap, (-val, key))
        result = []
        for i in range(k):
            result.append(heappop(max_heap)[1])
        
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent(["i","love","leetcode","i","love","coding"], 2))