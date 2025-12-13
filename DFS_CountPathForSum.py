class TreeNode:
 def __init__(self, val, left=None, right=None):
   self.val = val
   self.left = left
   self.right = right

class Solution:
    def countPaths(self, root, S):
        return self.countRec(root, S, [])

    def countRec(self, node, S, path):
        if not node:
            return 0

        path.append(node.val)
        path_sum = 0
        count = 0
        for i in range(len(path) - 1, -1, -1):
            path_sum += path[i]
            if path_sum == S:
                count += 1

        count += self.countRec(node.left, S, path)
        count += self.countRec(node.right, S, path)
        path.pop()

        return count

class Solution2:
    def countPaths(self, root, S):
        return self.countRec(root, S, 0, {0: 1})

    def countRec(self, node, target, running_sum, prefix_count):
        if not node:
            return 0

        running_sum += node.val
        count = prefix_count.get(running_sum - target, 0)

        prefix_count[running_sum] = prefix_count.get(running_sum, 0) + 1

        count += self.countRec(node.left, target, running_sum, prefix_count)
        count += self.countRec(node.right, target, running_sum, prefix_count)

        prefix_count[running_sum] -= 1

        return count

