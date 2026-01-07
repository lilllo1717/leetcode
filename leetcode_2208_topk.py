from heapq import *
import math

class Solution:
    def halveArray(self, nums):
        max_heap = [-x for x in nums]
        heapify(max_heap)
        num_operations = 0
        curr_sum = sum(nums)
        sum_to_reach = curr_sum/2

        while curr_sum > sum_to_reach:
            # print(max_heap)
            temp_el = -heappop(max_heap)
            temp_el /= 2
            heappush(max_heap, -temp_el)
            curr_sum -= temp_el
            num_operations +=1
        return num_operations

if __name__ == '__main__':
    sol = Solution()
    print(sol.halveArray([5,19,8,1]))