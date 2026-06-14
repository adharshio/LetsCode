class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        count=0
        answer=0
        for i in nums:
            count+=i
            if count==0:
                answer+=1
        return answer