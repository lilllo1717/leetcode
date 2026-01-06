class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        hashy = {0:1}
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in hashy:
                count += hashy[prefix_sum - k]
            if prefix_sum in hashy:
                hashy[prefix_sum] +=1
            else:
                hashy[prefix_sum] = 1
        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSubarrays([1,1,1], 2))
    print(sol.numberOfSubarrays([1,2,3], 3))