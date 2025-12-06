from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def findDepth(self, root):
    minimumTreeDepth = 0
    levels = []
    queue = deque()
    queue.append(root)
    # TODO: Write your code here
    while queue:
      minimumTreeDepth += 1
      levelSize = len(queue)
      for i in range(levelSize):
        currNode = queue.popleft()
        if not currNode.left and not currNode.right:
          return minimumTreeDepth
        if currNode.left:
          queue.append(currNode.left)
        if currNode.right:
          queue.append(currNode.right)


    return minimumTreeDepth

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(sol.findDepth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(sol.findDepth(root)))


main()