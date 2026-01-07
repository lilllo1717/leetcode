from heapq import *
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count_nums = Counter(nums)
        # print(count_nums)
        max_heap = []
        for key, val in count_nums.items():
            heappush(max_heap, (-val, key))

        # print(max_heap)
        result = []
        for i in range(k):
            result.append(heappop(max_heap)[1])
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))
    print(sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))
