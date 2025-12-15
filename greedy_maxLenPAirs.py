

class Solution:
    def findLongestChain(self, pairs):
        # ToDo: Write Your Code Here.
        pairs.sort(key=lambda x: x[1])

        count_chains = 0
        curr_end = float('-inf')

        for el in pairs:
            if el[0] > curr_end:
                curr_end = el[1]
                count_chains+=1

        print(pairs)


        return count_chains

solution = Solution()
example1 = [[1,2], [3,4], [2,3]]
example2 = [[5,6], [1,2], [8,9], [2,3]]
example3 = [[7,8], [5,6], [1,2], [3,5], [4,5], [2,3]]

print("Example 1:", solution.findLongestChain(example1))  # Expected Output: 2
print("Example 2:", solution.findLongestChain(example2))  # Expected Output: 3
print("Example 3:", solution.findLongestChain(example3))  # Expected Output: 3