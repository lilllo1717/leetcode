class Solution:
    def minMoves(self, nums):
        # ToDo: Write Your Code Here.
        max_num = None
        min_num = None
        str_len = len(nums)
        if str_len == 1:
            return 1
        for i, el in enumerate(nums):
            if max_num is None or el > max_num[0]:
                max_num = (el , i)
            if min_num is None or el < min_num[0]:
                min_num = (el, i)
        # print(max_num)
        # print(min_num)
        # print(str_len)
        min_dist_start = min_num[1] + 1
        min_dist_end = str_len - min_num[1]
        max_dist_start = max_num[1] + 1
        max_dist_end = str_len - max_num[1]
        

        total = min(max(min_dist_start, max_dist_start), min(min_dist_start + max_dist_end, min_dist_end + max_dist_start),
            max(min_dist_end, max_dist_end))
        
        return total


class Solution2:
    def minMoves(self, nums):
        n = len(nums)
        # Find the indexes of the minimum and maximum elements
        minIndex = nums.index(min(nums))
        maxIndex = nums.index(max(nums))

        # Calculate distances from both ends
        minDistStart = minIndex + 1
        minDistEnd = n - minIndex
        maxDistStart = maxIndex + 1
        maxDistEnd = n - maxIndex

        # Determine the most efficient sequence of moves
        totalMoves = min(
            max(minDistStart, maxDistStart),  # Both from start
            min(minDistStart + maxDistEnd, minDistEnd + maxDistStart),  # One from each end
            max(minDistEnd, maxDistEnd)  # Both from end
        )

        return totalMoves

# Testing the algorithm with example inputs
sol = Solution2()
print(sol.minMoves([3, 2, 5, 1, 4]))  # Output: 3
print(sol.minMoves([7, 5, 6, 8, 1]))  # Output: 2
print(sol.minMoves([2, 4, 10, 1, 3, 5]))  # Output: 4
