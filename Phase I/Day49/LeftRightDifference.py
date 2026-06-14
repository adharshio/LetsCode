class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            leftSum=0
            rightSum=0
            for j in range(i+1,n):
                rightSum+=nums[j]
            for k in range(0,i):
                leftSum+=nums[k]
            ans+=[abs(leftSum-rightSum)]
        return ans
