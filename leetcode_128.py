class Solution:
    def longestConsecutive(self, nums):
        # if not nums:
        #     return 0
        set_nums = set(nums)
        curr_longest = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                next_start = num
                while next_start in set_nums:
                    next_start += 1
                curr_longest = max(curr_longest, next_start - num)
            
        return curr_longest

if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))