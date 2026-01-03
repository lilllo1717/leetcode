class Solution:
    def dailyTemperatures(self, temperatures):
        # TODO: Write your code here
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx 
            stack.append(i)

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([70, 73, 75, 71, 69, 72, 76, 73])) # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    print(solution.dailyTemperatures([73, 72, 71, 70])) # Output: [0, 0, 0, 0]
    print(solution.dailyTemperatures([70, 71, 72, 73])) # Output: [1, 1, 1, 0]