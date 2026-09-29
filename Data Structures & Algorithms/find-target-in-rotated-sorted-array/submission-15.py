class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1

        while l <= h:
            m = (l + h) // 2
            print(l, h, m)
            if nums[m] == target:
                return m
            elif nums[l] <= target and nums[m] > target and nums[l] < nums[m]:
                h = m - 1
            elif nums[m] < target and nums[l] > target and nums[m] < nums[h]:
                l = m + 1
            elif nums[l] >= target and nums[l] > nums[m]: 
                h = m - 1
            else:
                l = m + 1
        
        return -1