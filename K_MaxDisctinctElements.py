from heapq import *
from collections import Counter

class Solution:
  def findMaximumDistinctElements(self, nums, k):
    distinctElementsCount = 0

    minHeap = []
    freqMap = Counter(nums)
    for num, freq in freqMap.items():
      if freq == 1:
        distinctElementsCount+=1
      else:
        heappush(minHeap, (freq, num))

    while k > 0 and minHeap:
      freq, num = heappop(minHeap)
      k -= freq - 1
      if k >= 0:
        distinctElementsCount+=1
    if k > 0:
      distinctElementsCount -= k

    return distinctElementsCount


def main():
  sol = Solution()
  print("Maximum distinct numbers after removing K numbers: " +
        str(sol.findMaximumDistinctElements([7, 3, 5, 8, 5, 3, 3], 2)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(sol.findMaximumDistinctElements([3, 5, 12, 11, 12], 3)))
  print("Maximum distinct numbers after removing K numbers: " +
        str(sol.findMaximumDistinctElements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2)))


main()