from heapq import *
from math import *

class Solution:
    def minStoneSum(self, piles, k):
        piles_heap = []
        for i in piles:
            heappush(piles_heap, -i)
        piles_heap = [-x for x in piles]
        heapify(piles_heap)
        print(piles_heap)
        while k > 0:
            # temp_val = piles_heap[0] - floor(piles_heap[0] / 2)
            # print("temp: ", temp_val)
            # heapreplace(piles_heap, piles_heap[0] - temp_val)
            temp_stone = heappop(piles_heap)
            temp_stone -= ceil(temp_stone *1/2)
            # print("temp: ", temp_stone)
            heappush(piles_heap, temp_stone)
            k -= 1
            # print("curr heap: ", piles_heap)
        return -sum(piles_heap)


if __name__ == "__main__":
    solution = Solution()
    print(solution.minStoneSum([5,4,9], 2))  # Output: 12
    print(solution.minStoneSum([4,3,6,7], 3))  # Output: 12