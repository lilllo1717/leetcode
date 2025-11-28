from collections import deque

Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def printLevelOrder(self, root):
        if root is None:
            return

        queue = deque()
        queue.append(root) 

        while queue:
            levelSize = len(queue)
            for _ in range(levelSize):
                node = queue.popleft()
                print(node.val, end=" ")

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

def main():
    # Example 1
    root1 = TreeNode(4)
    root1.left = TreeNode(5)
    root1.right = TreeNode(10)
    root1.left.left = TreeNode(5)
    root1.left.right = TreeNode(7)

    print("Example 1 Output: ", end="")
    Solution().printLevelOrder(root1)  # Expected Output: 4 5 10 5 7
    print()

    # Example 2
    root2 = TreeNode(5)
    print("Example 2 Output: ", end="")
    Solution().printLevelOrder(root2)  # Expected Output: 5
    print()

if __name__ == "__main__":
    main()
