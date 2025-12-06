from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None


class Solution:
  def findSuccessor(self, root, key):
    queue = deque()
    queue.append(root)
    return_sib = 0
    # TODO: Write your code here
    while queue:
      levSize = len(queue)
      for i in range(levSize):
        currNode = queue.popleft()
        if currNode.left:
          queue.append(currNode.left)
        if currNode.right:
          queue.append(currNode.right)
        if currNode.val == key:
          return queue.popleft()

    return root

def main():
    sol = Solutiion()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = sol.findSuccessor(root, 3)
    if result:
        print(result.val)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = sol.findSuccessor(root, 9)
    if result:
        print(result.val)

    result = sol.findSuccessor(root, 12)
    if result:
        print(result.val)


main()
