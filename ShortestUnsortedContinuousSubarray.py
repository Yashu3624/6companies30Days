class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        l = len(nums)-1
        u = 0 
        for i in range(len(nums)):
            if nums[i]!=sorted_nums[i]:
                l = min(l,i)
                u = max(i,u)
        return 0 if l>=u else u-l+1