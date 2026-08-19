class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        currMax = 0
        left = 0

        chars = {}


        for i,c in enumerate(s):

            if c not in chars:
                chars[c]=0
            chars[c]+=1

            worked = False

            for key in chars:
                first = chars[key]
                if i-left-first+1 <= k:
                    currMax = max(currMax, i-left+1)
                    worked = True   

            if not worked:
                chars[s[left]]-=1
                left += 1
                
        

        return currMax
            





        