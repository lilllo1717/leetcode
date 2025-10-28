# Given an array arr of unsorted numbers and a target sum, 
# count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, 
# and k are three different indices. Write a function to return the count of such triplets.

class Solution:
  def searchTriplets(self, arr, target):
    count = 0
    arr.sort()
    # current_min_sum = arr[0] + arr[1] + arr[2]
    for i in range(len(arr)):
      # if i > 0 and arr[i] == arr[i - 1]:
      #   continue
      count_update = self.findTripleSum(arr, target, i, i+1)
      count += count_update
    return count

  def findTripleSum(self, arr, target, i, left):
    n = len(arr)
    right = n - 1
    round_counter = 0
    while left < right:
      total_sum = arr[i] + arr[left] + arr[right]
      if total_sum < target:
        round_counter+= right-left
        left+=1
      else:
        right-=1
    return round_counter

def main():
  sol = Solution()
  print(sol.searchTriplets([-1, 0, 2, 3], 3))
  print(sol.searchTriplets([-1, 4, 2, 1, 3], 5))


main()