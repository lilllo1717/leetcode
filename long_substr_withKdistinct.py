class Solution1:
  def findLength(self, str1, k):
      max_length = 0
      windowStart = 0
      unique = {}

      for windowEnd in range(len(str1)):
          right_char = str1[windowEnd]
          if right_char not in unique:
              unique[right_char] = 0
          unique[right_char] += 1
          while len(unique) > k:
              left_char = str1[windowStart]
              unique[left_char] -= 1
              if unique[left_char] == 0:
                  del unique[left_char]
              windowStart += 1
          current_len = windowEnd - windowStart + 1
          if current_len > max_length:
              max_length = current_len

      return max_length

def main():
    sol = Solution()
    print("Length of the longest substring: "
          + str(sol.findLength("araaci", 2)))
    print("Length of the longest substring: "
          + str(sol.findLength("araaci", 1)))
    print("Length of the longest substring: "
          + str(sol.findLength("cbbebi", 3)))


main()