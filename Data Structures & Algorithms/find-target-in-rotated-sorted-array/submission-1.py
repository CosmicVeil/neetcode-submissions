class Solution:
    def search(self, nums: List[int], target: int) -> int:

        rotates = 0
        l = 0
        r = len(nums)-1

        if r == 0:
            if nums[0]==target:
                return 0
            else:
                return -1

        while l<=r:
            m = (l+r)//2

            if nums[m-1] > nums[m]:
                rotates = m
                break
            
            if nums[m] >= nums[0]:
                l = m+1
            else:
                r = m-1


        l = 0
        r = len(nums)-1

        while l<=r:

            m = (l+r)//2

            ind = (m+rotates) % len(nums)

            print(ind)
            print(rotates)

            if nums[ind]>target:
                r = m-1
            elif nums[ind]<target:
                l = m+1
            else:
                return ind
        
        return -1
