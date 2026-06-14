class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)-1):
            if 2*i<len(nums)-1:
                freq=nums[2*i]
                val=nums[2*i+1]
                for i in range(freq):
                    ans+=[val]
        return ans
