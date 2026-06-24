class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        n = len(s)
        r = 0
        hmap = {}
        maxLen =  1
        while r < n:
            hmap[s[r]] = hmap.get(s[r],0) + 1
            while hmap[s[r]] == 3:
                hmap[s[l]] -= 1
                l += 1
                
            maxLen = max(maxLen,r-l+1)
            r += 1
        print(hmap)
        return maxLen
            
