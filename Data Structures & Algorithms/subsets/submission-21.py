class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(acc, i):
            nonlocal ans
            if i == len(nums):
                ans.append(list(acc))
                return

            backtrack(acc, i + 1)
            acc.append(nums[i])
            backtrack(acc, i + 1)
            acc.pop()

        backtrack([], 0)
        return ans