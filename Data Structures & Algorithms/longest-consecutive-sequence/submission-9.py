class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sort = sorted(nums)
        ans = streak = 1

        for i, n in enumerate(sort):
            if i != 0:
                if n == sort[i - 1] + 1:
                    streak += 1
                elif n == sort[i - 1]:
                    continue
                else:
                    streak = 1
            if streak > ans:
                ans = streak

        return ans