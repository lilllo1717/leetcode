class Solution:
    def findMiddleIndex(self, nums) -> int:
        # ToDo: Write Your Code Here.
        leny = len(nums)
        totalSum = sum(nums)
        leftSum = 0

        for i, el in enumerate(nums):
            leftSum = leftSum + el
            rightSum = totalSum - leftSum + el

            if leftSum == rightSum:
                return i
        return -1

solution = Solution()
example1 = [1, 7, 3, 6, 5, 6]
example2 = [2, 1, -1]
example3 = [2, 3, 5, 5, 3, 2]
print(solution.findMiddleIndex(example1))  # Output: 3
print(solution.findMiddleIndex(example2))  # Output: 0
print(solution.findMiddleIndex(example3))  # Output: -1