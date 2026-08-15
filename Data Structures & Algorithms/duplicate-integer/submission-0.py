class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        occ = {}
        for a in nums:
            if a in occ:
                return True
            occ[a]=True

        return False
        