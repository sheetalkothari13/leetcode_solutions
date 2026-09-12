class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        copy = 0
        cnt = 0
        sorted_nums = sorted(nums)
        for num in sorted_nums:
            if copy == num:
                cnt += 1
                if cnt >= 2:
                    return True
            else:
                copy = num
                cnt = 1
        return False