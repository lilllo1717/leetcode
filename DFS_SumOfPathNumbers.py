class TreeNode:
 def __init__(self, val, left=None, right=None):
   self.val = val
   self.left = left
   self.right = right

class Solution:
  def findSumOfPathNumbers(self, root):
    # TODO: Write your code here
    total_sum = []
    self.findSumRecurs(root, total_sum, [], [])
    return sum(total_sum)

  def findSumRecurs(self, currNode, total_sum, pathSum, pathNodes):
    if currNode is None:
      return
    pathNodes.append(currNode.val)
    pathSum.append(currNode.val)
    if currNode.left is None and currNode.right is None:
      total_sum.append(self.convertToInt(pathSum))

    else:
      self.findSumRecurs(currNode.left, total_sum, pathSum, pathNodes)
      self.findSumRecurs(currNode.right, total_sum, pathSum, pathNodes)
    pathNodes.pop()
    pathSum.pop()

  def convertToInt(self, arrs):
    totalSum = 0
    lengy = len(arrs)
    for  i, el in enumerate(arrs):
      totalSum+= el*(10**(lengy-1-i))
    return totalSum


class Solution2:
  def findSumOfPathNumbers(self, root):
    return self.find_root_to_leaf_path_numbers(root, 0)

  def find_root_to_leaf_path_numbers(self, currentNode, pathSum):
    if currentNode is None:
      return 0

    # calculate the path number of the current node
    pathSum = 10 * pathSum + currentNode.val

    # if the current node is a leaf, return the current path sum
    if currentNode.left is None and currentNode.right is None:
      return pathSum

    # traverse the left and the right sub-tree
    return self.find_root_to_leaf_path_numbers(currentNode.left, pathSum) + \
                  self.find_root_to_leaf_path_numbers(currentNode.right, pathSum)


def main():
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(sol.findSumOfPathNumbers(root)))


main()