class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1 = 0
        cnt2 = 0
        current_num1 = 0
        current_num2 = 0
        res = []
        n = len(nums)
        for num in nums:
            if num == current_num1:
                cnt1 += 1
            elif num == current_num2:
                cnt2 += 1
            elif cnt1 == 0:
                current_num1 = num
                cnt1 = 1
            elif cnt2 == 0:
                current_num2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = nums.count(current_num1)
        cnt2 = nums.count(current_num2)

        if cnt1 > n//3:
            res.append(current_num1)
        if cnt2 > n//3 and current_num1 != current_num2:
            res.append(current_num2)
        return res