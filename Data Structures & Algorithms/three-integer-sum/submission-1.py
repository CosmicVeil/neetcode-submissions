class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        occ = {}
        ans = []
        for i,num in enumerate(nums):
            occ[num] = i
        
        used = {}
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                target = -nums[i]-nums[j]
                if target in occ and occ[target] > j:
                    ans.append([nums[i], nums[j], target])
        
        return ans