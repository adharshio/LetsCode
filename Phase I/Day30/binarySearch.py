class Solution:
    def search(self, nums: List[int], target: int) -> int:
        flag=0
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                flag=1
                return mid
        if flag==1:
            return mid
        else:
            return -1
