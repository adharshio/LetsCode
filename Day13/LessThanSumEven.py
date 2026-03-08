class Solution:
    def countEven(self, num: int) -> int:
        count=0
        def SumOfDigits(n):
            temp=0
            while n :
                digit=n%10
                temp+=digit
                n//=10
            return temp
        for i in range(1,num+1):
            dsum=SumOfDigits(i)
            if dsum%2==0:
                 count+=1
        return count
            
