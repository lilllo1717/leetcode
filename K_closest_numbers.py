from heapq import *
from collections import deque

class Solution:
  def findClosestElements(self, arr, K, X):
    
    heappy = []

    for i in range(len(arr)):
      heappush(heappy, (abs(arr[i] - X), arr[i]))
    
    new_arr = []
    for i in range(K):
      new_arr.append(heappop(heappy)[1])
    print(new_arr)

    # TODO: Write your code here
    return sorted(new_arr)



class Solution2:
  def findClosestElements(self, arr, K, X):
    index = self.binary_search(arr, X)
    low, high = index - K, index + K

    low = max(low, 0)

    high = min(high, len(arr) - 1)
    minHeap = []
    for i in range(low, high+1):
      heappush(minHeap, (abs(arr[i] - X), arr[i]))

    result = []
    for _ in range(K):
      result.append(heappop(minHeap)[1])

    result.sort()
    return result
  
  def binary_search(self, arr,  target):
    low, high = 0, len(arr) - 1
    while low <= high:
      mid = int(low + (high - low) / 2)
      if arr[mid] == target:
        return mid
      if arr[mid] < target:
        low = mid + 1
      else:
        high = mid - 1
    if low > 0:
      return low - 1
    return low


class Solution3:
  def findClosestElements(self, arr, K, X):
    result = deque()
    
    # Binary search to find the index of the element closest to X
    index = self.binary_search(arr, X)
    leftPointer, rightPointer = index, index + 1
    n = len(arr)
    
    for i in range(K):
      # Check if there are elements on both sides of the chosen element
      if leftPointer >= 0 and rightPointer < n:
        diff1 = abs(X - arr[leftPointer])
        diff2 = abs(X - arr[rightPointer])
        
        # Choose the element with the smaller absolute difference
        if diff1 <= diff2:
          result.appendleft(arr[leftPointer])  # Add the left element to the result
          leftPointer -= 1
        else:
          result.append(arr[rightPointer])  # Add the right element to the result
          rightPointer += 1
      # If there are no elements on one side, add elements from the other side
      elif leftPointer >= 0:
        result.appendleft(arr[leftPointer])
        leftPointer -= 1
      elif rightPointer < n:
        result.append(arr[rightPointer])
        rightPointer += 1

    return result


  def binary_search(self, arr,  target):
    low, high = 0, len(arr) - 1
    while low <= high:
      mid = int(low + (high - low) / 2)
      if arr[mid] == target:
        return mid
      if arr[mid] < target:
        low = mid + 1
      else:
        high = mid - 1
    if low > 0:
      return low - 1
    return low


def main():
  sol = Solution()
  print("'K' closest numbers to 'X' are: " +
        str(sol.findClosestElements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(sol.findClosestElements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(sol.findClosestElements([2, 4, 5, 6, 9], 3, 10)))


main()
