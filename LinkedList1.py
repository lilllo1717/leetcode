class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class Solution:
  def findMiddle(self, head):
    # 1 -> 2 -> 3 -> 4 -> 5 -> null
    slow, fast = head, head
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    return slow

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  # Print the middle node's value
  print("Middle Node: " + str(findMiddle(head).val))

  head.next.next.next.next.next = Node(6)
  # Print the middle node's value after adding a new node
  print("Middle Node: " + str(findMiddle(head).val))

  head.next.next.next.next.next.next = Node(7)
  # Print the middle node's value after adding another new node
  print("Middle Node: " + str(findMiddle(head).val))

# Call the main function to execute the code
main()