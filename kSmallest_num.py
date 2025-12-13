from heapq import *


class Solution:
  def findKthSmallestNumber(self, nums, k):
    maxHeap = []

    for i in range(k):
      heappush(maxHeap, -nums[i])
    print("maxHeap", maxHeap)
    for i in range(k, len(nums)):
      print("nums[i]: ",nums[i])
      if -nums[i] > maxHeap[0]:
        heappop(maxHeap)
        heappush(maxHeap, -nums[i])

    return -maxHeap[0]


def main():

  sol = Solution()

  print("Kth smallest number is: " +
        str(sol.findKthSmallestNumber([1, 5, 12, 2, 11, 5], 3)))

  print("Kth smallest number is: " +
        str(sol.findKthSmallestNumber([1, 5, 12, 2, 11, 5], 4)))

  print("Kth smallest number is: " +
        str(sol.findKthSmallestNumber([5, 12, 11, -1, 12], 3)))

  print("Kth smallest number is: " +
        str(sol.findKthSmallestNumber([-1, -2,-3,-4,-5], 5)))



main()