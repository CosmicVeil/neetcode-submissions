class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        initMap = {}
        secondMap = {}

        if len(s2) < len(s1): return False

        for c in s1:
            if c in initMap:
                initMap[c]+=1
            else:
                initMap[c] = 1
        

        for i in range(len(s1)):
            c = s2[i]
            if c in secondMap:
                secondMap[c]+=1
            else:
                secondMap[c] = 1
        
        if secondMap == initMap: return True

        for i in range(len(s1), len(s2)):
            secondMap[s2[i-len(s1)]]-=1

            if secondMap[s2[i-len(s1)]]==0:
                secondMap.pop(s2[i-len(s1)])

            if s2[i] not in secondMap: secondMap[s2[i]]=0
            secondMap[s2[i]]+=1

            if secondMap == initMap: return True
        

        return False

        