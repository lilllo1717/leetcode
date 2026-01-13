from heapq import *

class Solution:
    def kClosest(self, points, k) :
        min_heap = []
        result = []
        for nums in points:
            dist = (0 - nums[0])**2 + (0 - nums[1])**2
            heappush(min_heap, (dist, nums))
            # print(min_heap)
        while k > 0:
            result.append(heappop(min_heap)[1])
            k-=1
        # print(result)
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.kClosest([[1,3],[-2,2]], 1))
    print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))
