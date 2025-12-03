from collections import deque

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Pair:
    def __init__(self, node, index):
        self.node = node
        self.index = index

class Solution:
    # Method to find the maximum width of the binary tree
    def widthOfBinaryTree(self, root):
        # ToDo: Write Your Code Here.
        que = deque()
        que.append(Pair(root, 0))
        maxWidth = 0
  
        while que:
            levSize = len(que)
            minIndex = que[0].index
            first = 0
            last = 0
            for i in range(levSize):
                curr = que.popleft()
                currNode = curr.node
                index = curr.index - minIndex

                if i == 0:
                    first = index
                if i == levSize - 1:
                    last = index
                
                if currNode.left:
                    que.append(Pair(currNode.left, index * 2))
                if currNode.right:
                    que.append(Pair(currNode.right, index * 2 + 1))

            maxWidth = max(maxWidth, last - first + 1)
        return maxWidth


if __name__ == "__main__":
    sol = Solution()

    # Create the first example tree
    example1 = TreeNode(1)
    example1.left = TreeNode(2)
    example1.right = TreeNode(3)
    example1.left.left = TreeNode(4)
    example1.right.right = TreeNode(5)

    # Create the second example tree
    example2 = TreeNode(1)
    example2.left = TreeNode(2)
    example2.right = TreeNode(3)
    example2.left.left = TreeNode(4)
    example2.left.left.right = TreeNode(7)
    example2.right.left = TreeNode(5)
    example2.right.right = TreeNode(6)

    # Create the third example tree
    example3 = TreeNode(1)
    example3.left = TreeNode(2)
    example3.left.left = TreeNode(3)
    example3.left.right = TreeNode(4)
    example3.left.right.left = TreeNode(5)

    # Test the widthOfBinaryTree method with the example trees
    print(sol.widthOfBinaryTree(example1))  # Output: 4
    print(sol.widthOfBinaryTree(example2))  # Output: 4
    print(sol.widthOfBinaryTree(example3))  # Output: 2
