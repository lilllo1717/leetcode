class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # TODO: Write your code here
        stack  = []
        hashMap = {}
        result = []
        for num in nums2:
            while stack and stack[-1] < num:
                hashMap[stack.pop()] = num
            stack.append(num)
        
        for num in nums1:
            if num in hashMap:
                result.append(hashMap[num])
            else:
                result.append(-1)


        return result

sol = Solution()
print(sol.nextGreaterElement([9,7,1], [1,7,9,5,4,3]))