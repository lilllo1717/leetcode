
# Given an array of integers nums and an integer k,
#  find the length of the longest subarray that sums to k. 
# If no such subarray exists, return 0.

# class Solution:
#     def maxSubArrayLen(self, nums, k):
#         # ToDo: Write Your Code Here.
#         longest_seq = 0
#         for i, num in enumerate(nums):
#             print("i:", i, "value:", nums[i])
#             j = i + 1
#             while j < len(nums):
#                 summy = sum(nums[i:j+1])
#                 print(summy)
#                 if summy == k:
#                     new_seq_len = j - i + 1
#                     if new_seq_len > longest_seq:
#                         longest_seq = new_seq_len  
#                 j+=1
#         print("logest seq: ", longest_seq)
#         if longest_seq > 0:
#             return longest_seq
#         return 0

class Solution:
    def maxSubArrayLen(self, nums, k):
        max_len = 0
        cum_map = {}
        cum_sum = 0
        for i in range(len(nums)):
            cum_sum += nums[i]
            if cum_sum == k:
                max_len = i + 1
            if (cum_sum - k) in cum_map:
                diff = cum_sum - k
                max_len = max(max_len, i - cum_map[diff])
            if cum_sum not in cum_map:
                cum_map[cum_sum] = i
        
        if max_len > 0:
            return max_len
        return 0

if __name__ == "__main__":
    sol = Solution()

    # Test cases
    nums1 = [1, 2, 3, -2, 5]
    k1 = 5
    print(sol.maxSubArrayLen(nums1, k1))  # Output: 2

    nums2 = [-2, -1, 2, 1]
    k2 = 1
    print(sol.maxSubArrayLen(nums2, k2))  # Output: 2

    nums3 = [3, 4, 7, 2, -3, 1, 4, 2]
    k3 = 7
    print(sol.maxSubArrayLen(nums3, k3))  # Output: 4