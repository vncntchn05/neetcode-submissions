class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        ans = []
        
        for i, n in enumerate(sort):
            target = 0 - n
            l = i + 1
            r = len(sort) - 1
            
            while l < r:
                if sort[l] + sort[r] == target:
                    if [n, sort[l], sort[r]] not in ans:
                        ans.append([n, sort[l], sort[r]])
                    r -= 1
                    l += 1
                elif sort[l] + sort[r] > target:
                    r -= 1
                else:
                    l += 1
        
        return ans