class Solution:
    def containsDuplicate(self, nums):
        # count_nums = Counter(nums)
        # count = 0
        # for key, val in count_nums.items():
        #     if val >= 2:
        #         count+=1
        # if count > 0:
        #     return True
        # return False
        seen_nums = set()
        for num in nums:
            if num in seen_nums:
                return True
            seen_nums.add(num)
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))