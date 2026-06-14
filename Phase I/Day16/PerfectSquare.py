class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        else:
            s=1
            i=2
            while i*i<=num:
                if num%i==0 and (num//i)==i:
                     return True
                i+=1
            else:
                return False
