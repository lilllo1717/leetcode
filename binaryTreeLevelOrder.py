from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def traverse(self, root):
    result = []
    queue = deque()
    queue.append(root)
    count = 0
    # TODO: Write your code here
    while queue:
      currLevel = []
      levelSize = len(queue)
      for i in range(levelSize):
        currNode = queue.popleft()
        currLevel.append(currNode.val)
        if currNode.left:
          queue.append(currNode.left)
        if currNode.right:
          queue.append(currNode.right)
      if count % 2 != 0:
        result.append(list(reversed(currLevel)))
      else:
        result.append(currLevel)
      count +=1
      print(result)

    return result

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(sol.traverse(root)))


main()
