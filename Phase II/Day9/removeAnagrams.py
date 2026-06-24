class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        for i in range(n-1,0,-1):
            if sorted(words[i-1]) == sorted(words[i]):
                words.pop(i)
                n -= 1

        return words
