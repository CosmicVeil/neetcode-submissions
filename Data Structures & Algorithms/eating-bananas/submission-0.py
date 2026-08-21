class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = 1000000000

        minVal = r

        while l <= r:
            m = (l+r)//2

            if self.works(piles, m, h):
                minVal = m
                r = m-1

            else:
                l=m+1
        
        return minVal

    
    def works(self,piles, val, h):

        ans = 0

        for pile in piles:
            ans += math.ceil(pile/val)
        
        if ans <= h:
            return True
        else:
            return False



        