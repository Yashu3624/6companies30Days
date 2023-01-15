class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def Reverse(num):
            res = 0 
            while(num>0):
                rem = num%10
                num = num//10
                res = res*10 + rem
            return res
        map = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            left = nums[i] -Reverse(nums[i])
            count += map[left]
            map[left] += 1
        return count%((10**9)+7)
            
        