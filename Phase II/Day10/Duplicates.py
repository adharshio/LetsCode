class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        n = len(nums)
        ans = [] 

        for i in nums:
            if i in seen:
                ans += [i]
            seen.add(i)
        return ans
