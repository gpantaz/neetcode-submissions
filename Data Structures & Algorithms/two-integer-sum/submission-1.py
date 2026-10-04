class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        xx = {}
        for idx, num in enumerate(nums):
            xx[num - target] = idx

        for jdx, num in enumerate(nums):
            if -num in xx and jdx != xx[-num]:
                return sorted([xx[-num], jdx])
        return []