class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        s = 0
        for i in range(n):
            if nums[i] != val:
                nums[i],nums[s] = nums[s],nums[i]
                s += 1
        return s