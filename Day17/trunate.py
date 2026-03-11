class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        lstr=s.split()
        ans=""
        for i in range(k):
            ans+=lstr[i]
            if i!=k-1:
                ans+=" "
        return ans
