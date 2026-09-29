class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        if nums.count(0) > 1:
            return [0] * len(nums)

        with0 = 1
        without0 = 1
        for n in nums:
            with0 *= n
            if n != 0: 
                without0 *= n

        for n in nums:
            if n == 0:
                res.append(without0)
            else:
                res.append(with0 // n)

        return res
                