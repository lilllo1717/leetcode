#class TreeNode:
#  def __init__(self, val, left=None, right=None):
#    self.val = val
#    self.left = left
#    self.right = right

class Solution:
  def findPath(self, root, sequence):
    # TODO: Write your code here
    return self.findPrec(root, sequence, 0)

  def findPrec(self, currNode, sequence, i):
    # print("currNode: ", currNode.val)
    # print("i: ", i, "seq[i] = ", sequence[i])
    if currNode is None:
      return False
    if i >= len(sequence):
      return False
    if currNode.val != sequence[i]:
      print("wrong path for :", "currNode: ", currNode.val)
      return False
    if currNode.left is None and currNode.right is None:
      print("we found it")
      return i == len(sequence) - 1
    return self.findPrec(currNode.left, sequence, i+1) or self.findPrec(currNode.right, sequence, i+1)


def main():
  sol = Solution()
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(sol.findPath(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(sol.findPath(root, [1, 1, 6])))


main()