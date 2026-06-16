class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        i = 0
        n = len(words)
        m = len(s)

        if n != m:
            return False

        while i < n:
            if words[i][0] != s[i]:
                return False
            i += 1
        return True
