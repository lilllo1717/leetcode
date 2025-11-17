import math


class Solution1:
  def findMinSubArray(self, s, arr):
    # TODO: Write your code here
    windowSum = 0
    windowStart = 0
    min_len = len(arr)
    windowEnd = 0
    prev_end = 0
    if sum(arr) == s:
      return (len(arr))
    while windowEnd < len(arr):
      windowSum+= arr[windowEnd]
      if windowSum >= s:
        curr_len = windowEnd - windowStart + 1
        if curr_len < min_len:
          min_len = curr_len
        windowSum-=arr[windowStart]
        windowStart+=1
        windowSum-= arr[windowEnd]
        continue
      windowEnd+=1
    if min_len != len(arr) and windowEnd != len(arr) - 1:
      return min_len
    return 0   


import math

class Solution:
    def findMinSubArray(self, s, arr):
        window_sum = 0
        min_length = math.inf
        window_start = 0

        for window_end in range(0, len(arr)):
            window_sum += arr[window_end]
            while window_sum >= s:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= arr[window_start]
                window_start += 1
        
        if min_length == math.inf:
            return 0
        return min_length


def main():
    sol = Solution()
    print("Smallest subarray length: " + str(sol.findMinSubArray(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(sol.findMinSubArray(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(sol.findMinSubArray(8, [3, 4, 1, 1, 6])))

main()

