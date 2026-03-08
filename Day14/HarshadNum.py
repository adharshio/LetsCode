class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
         
        def SumOfDigits(n):
            temp=0
            if n<10:
                return n
            while n :
                digit=n%10
                temp+=digit
                n//=10
            return temp
        ans=SumOfDigits(x)
        if x%ans==0:
            return ans
        else:
            return -1
