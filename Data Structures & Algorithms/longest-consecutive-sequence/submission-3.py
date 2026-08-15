class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = sorted(list(set(nums)))

        if len(nums)==0:
            return 0

        maxConsec = 0
        currConsec = 1

        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                currConsec+=1
            else:
                maxConsec = max(maxConsec,currConsec)
                currConsec = 1
        
        maxConsec = max(maxConsec,currConsec)
        return maxConsec

        