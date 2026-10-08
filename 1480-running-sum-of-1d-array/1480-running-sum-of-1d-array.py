class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        n=len(nums)
        r=[0]*n
        for i in range(n):
            for j in range(i+1):
                r[i]+=nums[j]
        return r