from heapq import *

class Solution :
  def findKLargestNumbers(self, nums, k):
    # TODO: Write your code here
    # i = 0
    j = k
    chosen = nums[:k]
    # print(chosen)
    for i in range(k,len(nums)):
      if nums[i] > min(chosen):
        min_index = chosen.index(min(chosen))
        chosen[min_index] = nums[i]
    return chosen