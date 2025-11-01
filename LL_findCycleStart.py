
class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class Solution1:
  def findCycleStart(self, head):
    #TODO Write your code here
    slow = head
    fast =  head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        break
    else:
      return None
    slow  = head
    while fast != slow:
      slow = slow.next
      fast = fast.next
      
    return slow

class Solution2:
  def findCycleStart(self, head):
    cycle_length = 0

    # Find the LinkedList cycle using Floyd's Tortoise and Hare algorithm
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
      fast = fast.next.next  # Move two steps at a time
      slow = slow.next       # Move one step at a time
      if slow == fast:       # Found the cycle
        cycle_length = self.calculate_cycle_length(slow)
        break

    return self.find_start(head, cycle_length)

  def calculate_cycle_length(self, slow):
    current = slow
    cycle_length = 0

    # Calculate the length of the cycle by moving through it
    while True:
      current = current.next
      cycle_length += 1
      if current == slow:  # Reached back to the starting point of the cycle
        break

    return cycle_length

  def find_start(self, head, cycle_length):
    pointer1 = head
    pointer2 = head

    # Move pointer2 ahead 'cycle_length' nodes
    while cycle_length > 0:
      pointer2 = pointer2.next
      cycle_length -= 1

    # Increment both pointers until they meet at the start of the cycle
    while pointer1 != pointer2:
      pointer1 = pointer1.next
      pointer2 = pointer2.next

    return pointer1

def main():
  sol = Solution1()
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  # Create a cycle by connecting nodes
  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

  # Create a different cycle
  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

  # Create a cycle that points back to the head
  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(sol.findCycleStart(head).val))

main()