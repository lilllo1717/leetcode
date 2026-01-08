
from heapq import *

class Solution:
    def findKthLargest(self, nums, k) :
        # max_heap = []
        # for num in nums:
        #     heappush(max_heap, -num)
        # result = []
        # print(max_heap)
        # while max_heap:
        #     result.append(-heappop(max_heap))
        # print(result)
        # return result[k-1]

        # return nlargest(k, nums)[-1]
        print("nums: ", nums)
        min_heap = nums[:k]
        heapify(min_heap)
        print(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapreplace(min_heap, num)
            print("heap: ", min_heap)
        return min_heap[0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([3,2,1,5,6,4], 3))