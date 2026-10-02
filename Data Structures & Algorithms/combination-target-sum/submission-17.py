class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []

        def bt(i):
            nonlocal ans, subset
            if sum(subset) >= target or i == len(nums):
                if sum(subset) == target:
                    ans.append(list(subset))
                return

            subset.append(nums[i])
            bt(i)
            subset.pop()
            bt(i + 1)

        bt(0)
        return ans
