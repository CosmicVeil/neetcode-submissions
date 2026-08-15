class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for j,i in enumerate(numbers):
            val = target-i

            ind = self.binarySearch(numbers, j+1, len(numbers)-1,val)
            
            if ind != -1:
                return [j+1,ind+1]
        
        return [-1,-1]

    def binarySearch(self, arr, i, j, target):

        mid = int((i+j)/2)

        while i <= j:

            mid = int((i+j)/2)

            if arr[mid] < target:
                i=mid+1
            elif arr[mid]==target:
                return mid
            else:
                j=mid-1

        return -1

        
        