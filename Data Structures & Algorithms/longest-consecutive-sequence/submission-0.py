class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest = 0

        for num in unique_nums:
            if (num - 1) not in unique_nums:
                length = 1
                while (num + length) in unique_nums:
                    length += 1
                longest = max(length, longest)
        return longest