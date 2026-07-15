class Solution:
    def merge(self, nums, left, mid, right):
        temp = []

        i = left
        j = mid + 1

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1

        while i <= mid:
            temp.append(nums[i])
            i += 1

        while j <= right:
            temp.append(nums[j])
            j += 1

        for k in range(len(temp)):
            nums[left + k] = temp[k]
        
    def countPairs(self, nums, left, mid, right):
        count = 0
        j = mid + 1

        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))

        return count
    def mergeSort(self, nums, left, right):
        if left >= right:
            return 0

        mid = (left + right) // 2

        count = 0

        count += self.mergeSort(nums, left, mid)
        count += self.mergeSort(nums, mid + 1, right)
        count += self.countPairs(nums, left, mid, right)
        self.merge(nums, left, mid, right)

        return count

    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)