class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        subset = []

        def bt(i):
            nonlocal ans, subset
            if sum(subset) >= target or i == len(nums):
                if sum(subset) == target:
                    ans.append(subset.copy())
                return
                
            bt(i + 1)
            subset.append(nums[i])
            bt(i)
            subset.pop()

        bt(0)
        return ans
