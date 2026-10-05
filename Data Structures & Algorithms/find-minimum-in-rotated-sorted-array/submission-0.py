class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2
            # minimum is strictly to the right of middle
            if nums[middle] > nums[right]:
                left = middle + 1

            # middle could be the minimum, so keep it
            else:
                right = middle

        return nums[left]
