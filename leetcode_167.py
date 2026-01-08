class Solution:
    def twoSum(self, numbers, target):
        # print(numbers)
        i = 0
        j = len(numbers) - 1
        while j > i:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            if numbers[i] + numbers[j] < target:
                i+=1
            elif numbers[i] + numbers[j] > target:
                j-=1


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))