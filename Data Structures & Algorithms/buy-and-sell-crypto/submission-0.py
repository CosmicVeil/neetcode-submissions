class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ans = 0
        for i in range(len(prices)):
            curr = 0
            for j in range(i+1, len(prices)):
                curr = max(prices[j]-prices[i], curr)
            ans = max(ans,curr)
        
        return ans

                

        