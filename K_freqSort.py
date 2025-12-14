from heapq import *
from collections import Counter

class Solution:
  def sortCharacterByFrequency(self, str):
    mappy = Counter(str)
    print(mappy)
    heap = []
    new_string = ''
    for key, val in mappy.items():
      heappush(heap, (-val, key))
    for hi in heap:
      print(hi)
    for i in range(len(mappy)):
      times, letter = heappop(heap)
      new_string += ((-times)*letter)
    # print((new_string))
    return new_string

class Solution2:
  def sortCharacterByFrequency(self, str):

    charFrequencyMap = {}
    for char in str:
      charFrequencyMap[char] = charFrequencyMap.get(char, 0) + 1

    maxHeap = []
    for char, frequency in charFrequencyMap.items():
      heappush(maxHeap, (-frequency, char))

    sortedString = []
    while maxHeap:
      frequency, char = heappop(maxHeap)
      for _ in range(-frequency):
        sortedString.append(char)

    return ''.join(sortedString)


def main():
  sol = Solution()
  print("String after sorting characters by frequency: " +
        sol.sortCharacterByFrequency("Programming"))
  print("String after sorting characters by frequency: " +
        sol.sortCharacterByFrequency("abcbab"))


main()
