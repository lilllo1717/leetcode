class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def minRootToLeafSum(self, root):
        if root is None:
            return float('inf')

        if root.left is None and root.right is None:
            return root.val

        leftSum = self.minRootToLeafSum(root.left)
        rightSum = self.minRootToLeafSum(root.right)

        return root.val + min(leftSum, rightSum)
        
root1 = TreeNode(10)
root1.left = TreeNode(5)
root1.right = TreeNode(15)
root1.right.left = TreeNode(7)
root1.right.right = TreeNode(20)

root2 = TreeNode(-1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(1)

root3 = TreeNode(8)
root3.left = TreeNode(40)
root3.right = TreeNode(12)
root3.right.left = TreeNode(10)
root3.right.right = TreeNode(18)
root3.right.left.left = TreeNode(2)

solution = Solution()