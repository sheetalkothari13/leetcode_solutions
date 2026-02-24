class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = []
        neg = []
        res = []
        for num in nums:
            if num < 0:
                pos.append(num)
            else: 
                neg.append(num)
        for i in range(n):
            if i % 2 == 0:
                res.append(neg[i//2])
            else:
                res.append(pos[i//2])
        return res
