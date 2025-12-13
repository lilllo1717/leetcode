from heapq import *
from collections import Counter

class Solution:
  def findTopKFrequentNumbers(self, nums, k):
    topNumbers = []
    numbers = []
    num_dict = Counter(nums)
    for key, value in num_dict.items():
      heappush(numbers, (-value, key))
    for i in range(k):
      topNumbers.append(heappop(numbers)[1])
    print(topNumbers)
    # for num in nums:
    #   hashpush(numbers, num)
    # TODO: Write your code here
    return topNumbers



class Solution2:
  def findTopKFrequentNumbers(self, nums, k):

    # find the frequency of each number
    numFrequencyMap = {}
    for num in nums:
      numFrequencyMap[num] = numFrequencyMap.get(num, 0) + 1

    minHeap = []

    # go through all numbers of the numFrequencyMap and push them in the minHeap, which 
    # will have top k frequent numbers. If the heap size is more than k, we remove the 
    # smallest(top) number
    for num, frequency in numFrequencyMap.items():
      heappush(minHeap, (frequency, num))
      if len(minHeap) > k:
        heappop(minHeap)

    # create a list of top k numbers
    topNumbers = []
    while minHeap:
      topNumbers.append(heappop(minHeap)[1])

    return topNumbers


def main():
  sol = Solution()
  print("Here are the K frequent numbers: " +
        str(sol.findTopKFrequentNumbers([1, 3, 5, 12, 11, 12, 11], 2)))

  print("Here are the K frequent numbers: " +
        str(sol.findTopKFrequentNumbers([5, 12, 11, 3, 11], 2)))


main()
