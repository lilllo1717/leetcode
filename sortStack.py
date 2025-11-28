class Solution:
    def sortStack(self, stack):
        tempStack = []
        while stack:
            temp = stack.pop()
            while tempStack and tempStack[-1] > temp:
                stack.append(tempStack.pop())
            tempStack.append(temp)
        
        return tempStack

sol = Solution()
stack = [34, 3, 31, 98, 92, 23]
print("Input: ", stack)
print("Sorted Output: ", sol.sortStack(stack))