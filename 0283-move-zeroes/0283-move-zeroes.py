class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        s = 0 
        for i in range(n):
            if nums[i] != 0:
                nums[s],nums[i] = nums[i],nums[s]
                s+=1
        return nums