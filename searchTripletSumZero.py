
# Given an array of unsorted numbers, 
# find all unique triplets in it that add up to zero.

import math

class Solution:
  def searchTriplet(self, arr, target_sum):
    arr.sort()
    n = len(arr)
    curr_closest_sum = arr[0] + arr[1] + arr[2]
    for i in range(n - 2):
      if i > 0 and arr[i] == arr[i - 1]:
        continue
      round_result = self.searchT(arr, target_sum, i + 1, i)
      if (abs(round_result  - target_sum), round_result) < (abs(curr_closest_sum  - target_sum), curr_closest_sum):
        curr_closest_sum = round_result
      if curr_closest_sum == target_sum:
        return curr_closest_sum
    return curr_closest_sum
    
  def searchT(self, arr, target_sum, left, i):
    right = len(arr) - 1
    round_curr_sum = arr[i] + arr[left] + arr[right]
    while left < right:
      this_sum = arr[i] + arr[left] + arr[right]
      if abs(this_sum - target_sum) < abs(round_curr_sum  - target_sum):
        round_curr_sum = this_sum
      if this_sum < target_sum:
        left+=1
      elif this_sum > target_sum:
        right-=1
      else:
        return this_sum
    return round_curr_sum

def main():
  sol = Solution()
  print(sol.searchTriplet([-1, 0, 2, 3], 2))
  print(sol.searchTriplet([-3, -1, 1, 2], 1))
  print(sol.searchTriplet([1, 0, 1, 1], 100))
  print(sol.searchTriplet([0, 0, 1, 1, 2, 6], 5))


main()