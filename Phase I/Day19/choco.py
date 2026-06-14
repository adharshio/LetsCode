class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        count=0
        new_money=money
        for i in range(2):
            if new_money-min(prices)>=0:
                new_money=new_money-min(prices)
                count+=1
                mini=prices.index(min(prices))
                prices.pop(mini)
        if count==2:
            return new_money
        else:
            return money