class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n==2:
            return sorted(nums,reverse=True)
        new_nums=[]
        while nums:
            alice=min(nums)
            nums.remove(alice)
            bob=min(nums)
            new_nums.append(bob)
            new_nums.append(alice)
            nums.remove(bob)
        return new_nums