class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        ans = float("inf")
        while l <= h:
            mid = (l + h) // 2
            ans = min(ans, nums[mid])
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid - 1
            
        return ans