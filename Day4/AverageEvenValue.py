class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total_sum=0
        n=0
        for i in nums:
            if i%2==0 and i%3==0:
                n+=1
                total_sum+=i
        if n==0:
            return 0
        else:
            return total_sum//n