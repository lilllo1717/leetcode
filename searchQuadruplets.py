# Given an array of unsorted numbers and a target number, 
# find all unique quadruplets in it, whose sum is equal to the target number.

class Solution:
  def searchQuadruplets(self, arr, target):
    quadruplets = []
    # TODO: Write your code here
    n = len(arr)
    arr.sort()
    for i in range(n - 3):
      if i > 0 and arr[i] == arr[i - 1]:
        continue
      for j in range(i+ 1, n - 2):
        if j > i + 1 and arr[j] == arr[j - 1]:
          continue
        left = j + 1
        right = n - 1
        while left < right:
          curr_sum = arr[i] + arr[j] + arr[left] + arr[right]
          difference_with_target = target - (arr[i] + arr[j] + arr[right]) #1
          if target == curr_sum:
            quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
            lv, rv = arr[left], arr[right]
            while left < right and arr[left] == lv:
              left+=1
            while left < right and arr[right] == rv:
              right-=1
          elif curr_sum < target:
            left+=1
          else:
            right-=1
    return quadruplets


def main():
  sol = Solution()
  print(sol.searchQuadruplets([4, 1, 2, -1, 1, -3], 1))
  print(sol.searchQuadruplets([2, 0, -1, 1, -2, 2], 2))


main()
