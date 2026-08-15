class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        occ = {}
        arr = []

        for num in nums:
            if num in occ:
                occ[num]+=1
            else:
                occ[num]=1

        for key, value in occ.items():
            arr.append([value,key])

        arr.sort()
        arr.reverse()

        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        
        return ans

        