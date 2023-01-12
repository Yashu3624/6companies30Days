class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        divisibleSubset = [[num] for num in nums]
        
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] % nums[j]) == 0 and len(divisibleSubset[i]) < len(divisibleSubset[j]) + 1:
                    divisibleSubset[i] = divisibleSubset[j] + [nums[i]]
                    
        return max(divisibleSubset, key=len)