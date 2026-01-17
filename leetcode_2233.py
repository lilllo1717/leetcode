from heapq import *

class Solution:
    def maximumProduct(self, nums, k):
        max_heap = []
        for num in nums:
            heappush(max_heap, num)
        for i in range(k):
            temp = heappop(max_heap)
            # print("temp: ", temp) 
            temp += 1
            heappush(max_heap, temp)
            # print(max_heap)
        res = 1
        for x in max_heap:
            res = res*x % (10**9 +7)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.maximumProduct([6,3,3,2], 2))