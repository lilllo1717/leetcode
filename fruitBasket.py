import math

class Solution:
  def findLength(self, fruits):
      max_length = 0
      basket = {}
      start = 0
      for end in range(len(fruits)):
        right_el = fruits[end]
        if right_el not in basket:
          basket[right_el] = 0
        basket[right_el] += 1
        if len(basket) > 2:
          left_el = fruits[start]
          basket[left_el] -= 1
          if basket[left_el] == 0:
            del basket[left_el]
          start+=1

        curr_len = end - start + 1
        if curr_len > max_length:
          max_length = curr_len


      # TODO: Write your code here
      return max_length

def main():
    sol = Solution()
    print("Maximum number of fruits: "
          + str(sol.findLength(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: "
          + str(sol.findLength(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
