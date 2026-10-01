class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(acc, i):
            nonlocal ans
            if i == len(nums):
                ans.append(acc)
                return

            backtrack(list(acc), i + 1)
            acc.append(nums[i])
            backtrack(list(acc), i + 1)

        backtrack([], 0)
        return ans