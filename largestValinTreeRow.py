from typing import List
from collections import deque

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val: int):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:

    # Method to find the largest value in each row of the binary tree
    def largestValues(self, root: TreeNode) -> List[int]:
        result = []
        deq = deque()
        if root is None:
            return result
        deq.append(root)
        # result.append(root.val)
        while deq:
            levelSize = len(deq)
            levelNodes = []
            # if levelSize == 1:
            #     result.append(deq.popleft())
            for _ in range(levelSize):
                currNode = deq.popleft()
                levelNodes.append(currNode.val)
                if currNode.left:
                    deq.append(currNode.left)
                if currNode.right:
                    deq.append(currNode.right)
            result.append(max(levelNodes))
        print(result)
        return result


if __name__ == "__main__":
    solution = Solution()

    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(6)

    output1 = solution.largestValues(root1)
    print("Example 1 Output:", output1)  # Expected Output: [1, 3, 6]

    # Example 2
    root2 = TreeNode(7)
    root2.left = TreeNode(4)
    root2.right = TreeNode(8)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(5)
    root2.right.right = TreeNode(9)
    root2.left.left.right = TreeNode(3)

    output2 = solution.largestValues(root2)
    print("Example 2 Output:", output2)  # Expected Output: [7, 8, 9, 3]

    # Example 3
    root3 = TreeNode(10)
    root3.left = TreeNode(5)

    output3 = solution.largestValues(root3)
    print("Example 3 Output:", output3)  # Expected Output: [10, 5]
