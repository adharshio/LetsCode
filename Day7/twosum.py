class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=dict()
        for i in range(len(nums)):
            if target-nums[i] in seen:
                ans=target-nums[i]
                return i,seen[ans]
            else:
                 seen[nums[i]]=i
        