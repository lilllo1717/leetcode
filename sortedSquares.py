class Solution:
    def sortedSquares2(self, nums: List[int]) -> List[int]:
        new_arr = []
        for num in nums:
            new_arr.append(num*num)
        new_arr.sort()
        return new_arr
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return_arr = [0] * n
        write_pointer = n - 1
        left_p = 0
        right_p = n - 1
        left_value = nums[left_p] ** 2
        right_value = nums[right_p] ** 2
        while write_pointer >= 0:
            if left_value > right_value:
                return_arr[write_pointer] = left_value
                left_p+=1
                left_value = nums[left_p] ** 2
            else:
                return_arr[write_pointer] = right_value
                right_p-=1
                right_value = nums[right_p] ** 2
            write_pointer-=1
        return return_arr

        

def main():
    sol = Solution()
    nums = [-4,-1,0,3,10]
    print(sol.sortedSquares(nums))
main()
         
        