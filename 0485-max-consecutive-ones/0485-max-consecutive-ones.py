class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        max_consecutive = 0
        for num in nums:
            if num == 1:
                current += 1
                max_consecutive = max(current,max_consecutive)
            else:
                current = 0
        return max_consecutive 