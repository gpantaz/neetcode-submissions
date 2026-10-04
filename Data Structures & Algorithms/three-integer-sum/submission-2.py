class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # smallest value is positive, so no triplet can sum to 0
            if a > 0:
                continue  
            
            # skip duplicate first elements
            if i > 0 and a == nums[i - 1]:
                continue  

            l, r = i + 1, len(nums) - 1
            while l < r:
                total = a + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    # skip duplicate second elements
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res