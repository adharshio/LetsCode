class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans=0
        if ruleKey=="type":
            code=0
        elif ruleKey=="color":
            code=1
        else:
            code=2
        for i in items:
            if i[code]==ruleValue:
                ans+=1
        return ans
