class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        NoOfOnes=s.count("1")
        if NoOfOnes==1:
            return "0"*(len(s)-1)+"1"
        n=NoOfOnes
        return "1"*(n-1)+"0"*(len(s)-n)+"1"
