class Solution:
    def numberOfSubarrays(self, nums, k):
        nice_hash = {0:1}
        count = 0
        pref_sum = 0
        for num in nums:
            pref_sum += (num % 2)
            if pref_sum - k in nice_hash:
                count += nice_hash[pref_sum - k]
            if pref_sum in nice_hash:
                nice_hash[pref_sum] += 1
            else:
                nice_hash[pref_sum] = 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.numberOfSubarrays([1,1,2,1,1], 3))
    print(sol.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))
