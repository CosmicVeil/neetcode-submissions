class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        rotates = 0
        l = 0
        r = len(nums)-1

        if r == 0:
            return nums[0]

        while l<=r:
            m = (l+r)//2

            if nums[m-1] > nums[m]:
                rotates = m
                break
            
            if nums[m] >= nums[0]:
                l = m+1
            else:
                r = m-1

        
        
        return nums[rotates]

            

