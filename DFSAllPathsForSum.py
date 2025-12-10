class TreeNode:
 def __init__(self, val, left=None, right=None):
   self.val = val
   self.left = left
   self.right = right

class Solution:
  def findPaths(self, root, required_sum):
    allPaths = []
    self.dfs(root, allPaths, [], required_sum)
    return allPaths


  def dfs(self, currNode, allPaths, currentPath, required_sum):
    if currNode is None:
      return
    currentPath.append(currNode.val)
    # TODO: Write your code here
    if currNode.val == required_sum and currNode.left is None and currNode.right is None:
      allPaths.append(list(currentPath))
    else:
      self.dfs(currNode.left, allPaths, currentPath, required_sum - currNode.val)
      self.dfs(currNode.right, allPaths, currentPath, required_sum - currNode.val)
    currentPath.pop()

def main():
  sol = Solution()
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(sol.findPaths(root, required_sum)))


main()
