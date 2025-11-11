# Any number will be called a happy number if, 
# after repeatedly replacing it with a number equal to the sum 
# of the square of all of its digits, leads us to the number 1. 
# All other (not-happy) numbers will never reach 1. Instead, they 
# will be stuck in a cycle of numbers that does not include 1.


# Given a positive number n, return true if it is a happy number
#  otherwise return false.


class Solution1:
  def __init__(self):
    self.num_map = {}
  def find(self, num):
    # TODO: Write your code here
    sq_digits = [int(d)**2 for d in str(num)]
    sum_sq_digits = sum(sq_digits)
    if sum_sq_digits == 1:
      return True
    if sum_sq_digits in self.num_map:
      return False
    self.num_map[sum_sq_digits] = True
    return self.find(sum_sq_digits)


class Solution2:
  def find(self, num):
    slow, fast = num, num
    while True:
      slow = self.find_square_sum(slow)  # move one step
      fast = self.find_square_sum(self.find_square_sum(fast))  # move two steps
      if slow == fast:  # found the cycle
        break
    return slow == 1  # see if the cycle is stuck on the number '1'


  def find_square_sum(self, num):
    _sum = 0
    while (num > 0):
      digit = num % 10
      _sum += digit * digit
      num //= 10
    return _sum


def main():
  sol = Solution1()
  print(sol.find(23))
  print(sol.find(12))


main()