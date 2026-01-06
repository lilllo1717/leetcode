class Solution:
    def checkSubarraySum(self, nums, k) -> bool:

        subs_hash = {0:-1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            needed_diff = prefix_sum%k
            # print("nprefix_sum: ", prefix_sum) 
            # print("needed diff: ", needed_diff)

            if needed_diff in subs_hash and i - subs_hash[needed_diff]>= 2:
                return True
            elif needed_diff not in subs_hash:
                subs_hash[needed_diff] = i
            # print(subs_hash)
        return False            


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkSubarraySum([23,2,4,6,7], 6))
    print(sol.checkSubarraySum([23,2,6,4,7], 6))
    print(sol.checkSubarraySum([23,2,6,4,7], 13))
