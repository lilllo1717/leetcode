from heapq import *
from math import *

class Solution:
    def maxKelements(self, nums, k):
        score = 0
        heap = [-x for x in nums]
        heapify(heap)
        # print(heap)
        while k > 0:
            new_num = heappop(heap)
            score += new_num
            new_num = ceil(new_num // 3)
            # print(new_num)
            heappush(heap, new_num)
            # print("new heap: ", heap)
            k-=1
        return -score

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxKelements([1,10,3,3,3], 3))