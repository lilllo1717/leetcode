import math

class Solution:
  def sort(self, arr):
    # TODO: Write your code here
    n = len(arr)
    if n <= 1:
      return 0
    left = 0
    while left+ 1 < n and arr[left] <=arr[left+1]:
      left+=1
    if left == n-1:
      return 0
    right = n -1
    while right - 1 and arr[right] >= arr[right - 1]:
      right-=1
    min_in_subarr = min(arr[left:right+1])
    max_in_subarr = max(arr[left:right+1])
    while left > 0 and arr[left - 1] > min_in_subarr:
      left-=1
    while right < n -  1 and arr[right + 1] < max_in_subarr:
      right+=1
    return right - left + 1


def main():
  sol = Solution()
  print(sol.sort([1, 2, 5, 3, 7, 10, 9, 12]))
  print(sol.sort([1, 3, 2, 0, -1, 7, 10]))
  print(sol.sort([1, 2, 3]))
  print(sol.sort([3, 2, 1]))


main()