class Solution:
    def findGCD(self, nums: List[int]) -> int:
        num1=max(nums)
        num2=min(nums)
        answer=1
        for i in range(1,num2+1):
            if num2%i==0 and num1%i==0:
                answer=i
        return answer