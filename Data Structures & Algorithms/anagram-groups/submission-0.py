class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagramDict = {}

        for s in strs:
            sortedS = "".join(sorted(s))

            if sortedS in anagramDict:
                anagramDict[sortedS].append(s)
            else:
                anagramDict[sortedS] = [s];
        

        outputArray = []

        for key in anagramDict:
            currArray = []

            for val in anagramDict[key]:
                currArray.append(val)
            
            outputArray.append(currArray)
        

        return outputArray
        