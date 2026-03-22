class Solution:
    def fib(self, n: int) -> int:
        def answer(n):
            if n==0:
                return 0
            if n==1:
                return 1
            return answer(n-1)+answer(n-2)
        ans=answer(n)
        return ans
