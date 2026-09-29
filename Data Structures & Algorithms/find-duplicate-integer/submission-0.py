class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = [False] * 10000
        
        for n in nums:
            if freq[n]:
                return n
            freq[n] = True