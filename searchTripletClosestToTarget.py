# Given an array of unsorted numbers and a target number, 
# find a triplet in the array whose sum is as close to the 
# target number as possible, return the sum of the triplet. 
# If there are more than one such triplet, return the sum of 
# the triplet with the smallest sum.


class Solution:
    def searchTriplets(self, arr):
        triplets = []
        arr.sort()
        n = len(arr)
        for i in range(len(arr) - 2):
            if arr[i] > 0:
                break
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            if arr[i] + arr[i + 1] + arr[i + 2] > 0:
                break
            if arr[i] + arr[n - 2] + arr[n - 1] < 0:
                continue
            self.searchy(-arr[i], arr, i + 1, triplets)
        return triplets
    def searchy(self, target, arr, left, triplets):
        right = len(arr) - 1
        while (left < right):
            curr_sum = arr[left] + arr[right]
            if curr_sum == target:
                triplets.append([-target, arr[left], arr[right]])
                left+=1
                right-=1
                while left < right and arr[left] == arr[left - 1]:
                    left+=1
                while left < right and arr[right] == arr[right + 1]:
                    right-=1
            elif curr_sum < target:
                left+=1
            else:
                right-=1

def main():
  sol = Solution()
  print(sol.searchTriplets([-3, 0, 1, 2, -1, 1, -2]))
  print(sol.searchTriplets([-5, 2, -1, -2, 3]))


main()