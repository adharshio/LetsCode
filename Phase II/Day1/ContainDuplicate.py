class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for I in nums :
            if I in seen:
                return True
            seen.add(I)
        return False
