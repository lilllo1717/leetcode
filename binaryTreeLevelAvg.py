from collections import deque


#class TreeNode:
#  def __init__(self, val):
#    self.val = val
#    self.left, self.right = None, None

class Solution:
  def findLevelAverages(self, root):
    result = []
    queue = deque()
    queue.append(root)
    # TODO: Write your code here
    while queue:
      levelSize = len(queue)
      currLevel = []
      for i in range(levelSize):
        currNode = queue.popleft()
        currLevel.append(currNode.val)

        if currNode.left:
          queue.append(currNode.left)
        if currNode.right:
          queue.append(currNode.right)
      avg = sum(currLevel)/len(currLevel)
      result.append(avg)
      print(result)
    return result

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(sol.findLevelAverages(root)))


main()