class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        if n==1:
            return [0]
        if n%2==0:
            for i in range(1,(n//2)+1):
                ans+=[i]
                ans+=[i*(-1)]
        else:
            for i in range(1,(n//2)+1):
                ans+=[i]
                ans+=[i*(-1)]
            ans+=[0]
        return ans
