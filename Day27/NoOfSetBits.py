class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_val=str(bin(n))
        return binary_val.count("1")
