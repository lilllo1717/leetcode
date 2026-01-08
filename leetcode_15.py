class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            k = len(nums) - 1
            j = i+1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j < k and nums[j] == nums[j -1]:
                        j+=1
                    while j < k and nums[k] == nums[k + 1]:
                        k-=1
                elif total > 0:
                    k-=1
                elif total < 0:
                    j+=1
        # print(nums)
        return result

if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))