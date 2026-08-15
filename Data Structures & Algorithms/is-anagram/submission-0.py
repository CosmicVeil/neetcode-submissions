class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if(len(s)!=len(t)):
            return False

        charMapS = {}
        charMapT = {}

        for c in s:
            if c in charMapS:
                charMapS[c]+=1
            else:
                charMapS[c]=1

        for c in t:
            if c in charMapT:
                charMapT[c]+=1
            else:
                charMapT[c]=1

        if charMapT == charMapS:
            return True
        return False





        