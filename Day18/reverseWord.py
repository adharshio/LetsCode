class Solution:
    def reverseWords(self, s: str) -> str:
        new=s.split()
        ans=""
        for i in range(len(new)):
            ans+=new[i][::-1]
            if i!=len(new)-1:
                ans+=" "
        return ans