from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        # ToDo: Write Your Code Here.
        queue = deque()
        queue.append(root)
        answers = []
        level = 0
        print("\n")
        while queue:
            levelNodes = []
            levelSize = len(queue)
            for i in range(levelSize):
                currNode = queue.popleft()
                # print("currNode: ",currNode.val)
                levelNodes.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            print("nodes: ", levelNodes)
            if level%2 == 0:
                sorted_asc = sorted(levelNodes)
                if sorted_asc == levelNodes and all(val % 2 == 1 for val in levelNodes):
                    answers.append(1)
                else:
                    return False
            else:
                sorted_desc = sorted(levelNodes, reverse = True)
                print("sorted_desc: ", sorted_desc)
                print("levelNodes: ", levelNodes)
                if sorted_desc == levelNodes and all(val % 2 == 0 for val in levelNodes):
                    answers.append(1)
                else:
                    return False
            level+=1
        print("answers: ", answers)
        if 0 in answers:
            return False
        return True


class Solution2:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        level = 0
        
        while queue:
            size = len(queue)
            values = []
            
            for _ in range(size):
                node = queue.popleft()
                values.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level % 2 == 0:
                for i in range(len(values)):
                    if values[i] % 2 == 0 or (i > 0 and values[i] <= values[i - 1]):
                        return False
            else:
                for i in range(len(values)):
                    if values[i] % 2 != 0 or (i > 0 and values[i] >= values[i - 1]):
                        return False
            level += 1
        
        return True

# Example usage
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    root1 = TreeNode(1)
    root1.left = TreeNode(10)
    root1.right = TreeNode(4)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(7)
    print(sol.isEvenOddTree(root1))  # Output: true
    
    # Example 2
    root2 = TreeNode(5)
    root2.left = TreeNode(9)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(12)
    root2.right.right = TreeNode(8)
    print(sol.isEvenOddTree(root2))  # Output: false
    
    # Example 3
    root3 = TreeNode(7)
    root3.left = TreeNode(10)
    root3.right = TreeNode(2)
    root3.left.left = TreeNode(12)
    root3.left.right = TreeNode(8)
    print(sol.isEvenOddTree(root3))  # Output: false