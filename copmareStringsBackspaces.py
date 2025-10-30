# Given two strings containing backspaces (identified by the character ‘#’), 
# check if the two strings are equal.

# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.


class Solution1:
  def compare(self, str1, str2):
    # TODO: Write your code here
    def build(strin):
      stack = []
      for ch in strin:
        if ch != '#':
          stack.append(ch)
        elif stack:
          stack.pop()
      return ''.join(stack)
    return build(str1) == build(str2)

class Solution2:
  def compare(self, str1, str2):
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    while index1 >= 0 or index2 >= 0:
      i1 = self.get_next_valid_index(index1, str1)
      i2 = self.get_next_valid_index(index2, str2)
      if i1 < 0 and i2 < 0:
        return True
      if i1 < 0 or i2 < 0:
        return False
      if str1[i1] != str2[i2]:
        return False
      index1 = i1 - 1
      index2 = i2 - 1
    return True
  def get_next_valid_index(self, indexy, stringy):
    backspace_count = 0
    while indexy >= 0:
      if stringy[indexy] == '#':
        backspace_count+=1
        indexy-=1
      elif backspace_count > 0:
        backspace_count-=1
        indexy-=1
      else:
        break
    return indexy


def main():
  sol = Solution2()
  print(sol.compare("xy#z", "xzz#"))
  print(sol.compare("xy#z", "xyz#"))
  print(sol.compare("xp#", "xyz##"))
  print(sol.compare("xywrrmp", "xywrrmu#p"))


main()

