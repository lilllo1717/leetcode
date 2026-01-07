

class Solution:
    def checkArray(self, nums, k) -> bool:
        n = len(nums)
        delta = [0] * (n + 1)
        cur_sum = 0 # This tracks the net effect of ongoing subtractions

        for i in range(n):
            cur_sum += delta[i]
            # Current value after applying all previous windows
            needed = nums[i] + cur_sum 
            
            if needed == 0:
                continue
            
            # Since we can only subtract, 'needed' must be positive
            # And we must have space to start a window of size k
            if needed < 0 or i + k > n:
                return False
            
            # Apply a subtraction of 'needed' starting at i and ending at i+k-1
            cur_sum -= needed
            if i + k < n:
                delta[i + k] += needed

        return True                                                         

class Solution2:
    def checkArray(self, nums, k) -> bool:
        diff_arr = [0] * (len(nums) + 1)
        pref_sum = 0

        for i in range(len(nums)):
            pref_sum += diff_arr[i]
            current = nums[i] - pref_sum

            if current < 0:
                return False
            if current > 0:
                if i + k > len(nums):
                    return False
                diff_arr[i + k] -= current
                pref_sum += current

        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.checkArray([2,2,3,1,1,0], 3))
    print(sol.checkArray([1,3,1,1], 2))