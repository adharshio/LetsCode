class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        Sinteger=""
        for i in digits:
            Sinteger+=str(i)
        integer=int(Sinteger)
        integer+=1
        Sinteger=str(integer)
        ans=[]
        for i in Sinteger:
            ans+=[int(i)]
        return ans
