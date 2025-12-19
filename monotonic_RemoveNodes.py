class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

class Solution:
    def removeNodes(self, head):
        # TODO: Write your code here
        stack = []
        curr = head

        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            if stack:
                stack[-1].next = curr
            stack.append(curr)
            curr = curr.next

        return stack[0] if stack else None

solution = Solution()

head1 = Node(5)
head1.next = Node(3)
head1.next.next = Node(7)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(2)
head1.next.next.next.next.next = Node(1)
head1 = solution.removeNodes(head1)

# Printing the modified list: 7 -> 4 -> 2 -> 1
node = head1
while node:
    print(node.val, end=" -> " if node.next else "\n")
    node = node.next