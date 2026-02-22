class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        major_num = 0
        for num in nums:
            if cnt == 0:
                major_num = num
                cnt += 1
            elif major_num == num:
                cnt += 1
            else:
                cnt -= 1
        return major_num