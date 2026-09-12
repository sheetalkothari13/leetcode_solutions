class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        left = self.leftproduct(nums)
        right = self.rightproduct(nums)
        for i in range(n):
            answer[i] = left[i] * right[i]
        return answer
    
    def leftproduct(self,nums):
        n = len(nums)
        left = [1] * n
        product = 1
        for i in range(n):
            left[i] = product
            product *= nums[i]
        return left
    
    def rightproduct(self,nums):
        n = len(nums)
        right = [1] * n
        product = 1
        for i in range(n-1,-1,-1):
            right[i] = product
            product *= nums[i]
        return right
