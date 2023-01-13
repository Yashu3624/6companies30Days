class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        import math
        nums = sorted(nums)
        GCD = math.gcd(*numsDivide)
        count = 0
        for i in nums:
            if GCD%i==0:
                break
            else:
                count+=1
        if count == len(nums):
            return -1
        else:
            return count
        