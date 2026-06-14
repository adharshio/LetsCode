class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        def sumOfDigits(n):
            sum_val=0
            while n:
                digit=n%10
                sum_val+=digit
                n//=10
            return sum_val
        digits_value=0
        tot_sum=0
        for i in nums:
            tot_sum+=i
            digits_value+=sumOfDigits(i)
        return abs(tot_sum-digits_value)