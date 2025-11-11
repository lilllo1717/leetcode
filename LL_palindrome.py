class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class Solution:
  def isPalindrome(self, head):
    # TODO: Write your code here
    start = head
    while start:
      start = start.next
    slow = head
    fast = slow.next
    last_equal = None
    while slow:
      if fast == last_equal:
        return True
      if fast.next == last_equal and slow.next == fast and slow.val == fast.val:
        return True
      if last_equal:
        while fast.next != last_equal:
          fast = fast.next
      else:
        while fast.next:
          fast = fast.next
      if slow.val != fast.val:
        return False
      else:
        slow = slow.next
        last_equal = fast
        fast = slow.next
    return True


class Solution2:
  def isPalindrome(self, head):
    if head is None or head.next is None:
      return True

    # find middle of the LinkedList
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
      slow = slow.next
      fast = fast.next.next

    head_second_half = self.reverse(slow)  # reverse the second half
    # store the head of reversed part to revert back later
    copy_head_second_half = head_second_half

    # compare the first and the second half
    while (head is not None and head_second_half is not None):
      if head.val != head_second_half.val:
        break  # not a palindrome

      head = head.next
      head_second_half = head_second_half.next

    self.reverse(copy_head_second_half)  # revert the reverse of the second half

    if head is None or head_second_half is None:  # if both halves match
      return True

    return False


  def reverse(self, head):
    prev = None
    while (head is not None):
      next = head.next
      head.next = prev
      prev = head
      head = next
    return prev


# tests 
def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head

def run_test(values, expected):
    head = build_list(values)
    sol = Solution()
    print(f"Test: {values}")
    try:
        result = sol.isPalindrome(head)
        print(f"Result: {result}, Expected: {expected}")
    except Exception as e:
        print(f"Raised exception: {e}, Expected: {expected}")
    print("-" * 40)

# 1. Empty list
run_test([], True)

# 2. Single element
run_test([1], True)

# 3. Two equal elements (palindrome)
run_test([1, 1], True)

# 4. Two different elements (not palindrome)
run_test([1, 2], False)

# 5. Odd length palindrome
run_test([1, 2, 1], True)

# 6. Odd length, not palindrome
run_test([1, 2, 3], False)

# 7. Even length palindrome
run_test([1, 2, 2, 1], True)

# 8. Even length, not palindrome
run_test([1, 2, 3, 4], False)

# 9. Palindrome with repeating blocks
run_test([1, 1, 2, 2, 1, 1], False)   # not symmetric

# 10. Longer palindrome
run_test([1, 2, 3, 2, 1], True)

# 11. Longer not palindrome
run_test([1, 2, 3, 4, 1], False)
