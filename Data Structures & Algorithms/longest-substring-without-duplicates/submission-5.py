class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        curr_length = 0

        left = 0

        used = {}

        for i,c in enumerate(s):

            if c in used and used[c] >= left:
                length = max(length, curr_length)
                curr_length = i-used[c]

                left = used[c]+1
                
                used[c]=i
                

            else:
                used[c]=i
                curr_length+=1
        
        length = max(length,curr_length)
        return length

        