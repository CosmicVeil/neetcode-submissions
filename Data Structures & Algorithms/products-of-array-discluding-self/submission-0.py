class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suff=[1]*len(nums)

        for i in range(len(nums)):
            pref.append(pref[i]*nums[i])
        

        for i in range(len(nums)-1,0,-1):
            suff[i-1] = suff[i]*nums[i]
        
        ans = []

        for i in range(len(nums)):
            ans.append(pref[i]*suff[i])
        
        return ans
        

        