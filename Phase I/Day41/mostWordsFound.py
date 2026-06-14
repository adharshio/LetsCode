class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer=0
        maxcount=-1
        for i in sentences:
            count=0
            words=i.split()
            for i in words:
                count+=1
            if count>maxcount:
                maxcount=count
        return maxcount
