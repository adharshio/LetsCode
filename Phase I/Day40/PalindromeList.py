class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindrome(s):
            n=len(s)
            for i in range(0,n,1):
                if s[i]!=s[n-i-1]:
                    return ""
            return s
        for i in words:
            ans=isPalindrome(i)
            if ans!="":
                break
        return ans

        
