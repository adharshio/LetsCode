class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            SetBits=str(bin(i))
            count=SetBits.count("1")
            if count==k:
                ans+=nums[i]
        return ans
