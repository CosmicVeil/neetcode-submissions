class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            curr = nums[i]

            try:
                idx = nums.index(target-curr, i+1)
            except ValueError:
                continue
            
            return [i,idx]

        