from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root):
        # ToDo: Write Your Code Here.
        queue = deque()
        queue.append(root)
        maxLevelSum = 0
        currLevel = 1
        returnLevel = 1
        while queue:
            levelSize = len(queue)
            levelNodes = []
            
            for i in range(levelSize):
                currNode = queue.popleft()
                levelNodes.append(currNode.val)

                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            
            if sum(levelNodes) > maxLevelSum:
                returnLevel = currLevel
                maxLevelSum = sum(levelNodes)
            currLevel+=1
        return returnLevel

if __name__ == "__main__":
    solution = Solution()

    # Example 1
    example1 = TreeNode(1)
    example1.left = TreeNode(20)
    example1.right = TreeNode(3)
    example1.left.left = TreeNode(4)
    example1.left.right = TreeNode(5)
    example1.right.right = TreeNode(8)
    print(solution.maxLevelSum(example1))  # Output: 2