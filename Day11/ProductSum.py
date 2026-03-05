class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_val=0
        prod_val=1
        temp=n
        while temp:
            digit=temp%10
            temp//=10
            sum_val+=digit
            prod_val*=digit
        return prod_val-sum_val
        
