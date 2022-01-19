class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0; e=0; sums=0; ans =10**9
        while e < len(nums):
            while e < len(nums) and sums < target:
                sums += nums[e]
                e += 1
            while s < e and sums >= target:
                ans = min(ans, e - s)
                sums -= nums[s]
                s += 1
        if(ans==10**9):return 0
        else:return ans