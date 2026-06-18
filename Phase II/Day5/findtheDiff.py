class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        ans = ""
        seen={}
        for i in t:
            seen[i] = seen.get(i,0) + 1
        for j in s:
            seen[j] -= 1
        print(seen)
        for k in t:
            if seen[k]  > 0:
                ans += k
                seen[k] -= 1
                
        return ans

        # seen = {}
        # for i in t:
        #     seen[i] = 1
        # for i in s:
        #     seen[i] = 0
        # for i in t:
        #     if seen[i] == 1:
        #         ans += i
        # return ans
