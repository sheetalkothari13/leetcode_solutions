class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums) 
        if n <= 1:
            return True
        cnt = 0
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                cnt += 1
                if cnt == 1:
                    if nums[(i+1) % n] > nums[0]:
                        return False
                if cnt > 1:
                    return False
        return True

