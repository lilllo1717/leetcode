from heapq import *

class Solution:
    def findClosestElements(self, arr, k, x):

        heapy = []
        result = []

        for num in arr:
            heappush(heapy, (abs(num -x), num))
        # print(heapy)
        for i in range(k):
            temp = heappop(heapy)
            result.append(temp[1])
        # print(sorted(result))
        return sorted(result)

class Solution2:
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr) - 1

        while right - left >= k:
            if abs(arr[left] - x) <= abs(arr[right] - x):
                right -= 1
            
            else:
                left += 1
        
        return arr[left: right + 1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.findClosestElements([1,2,3,4,5],4,3))