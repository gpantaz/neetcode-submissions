class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return

            for jdx in range(idx, len(nums)):
                if total + nums[jdx] > target:
                    return
                cur.append(nums[jdx])
                dfs(jdx, cur, total + nums[jdx])
                cur.pop()

        dfs(0, [], 0)
        return res