class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        r = len(matrix)-1

        ind = -1

        while l <= r:
            m = (l+r)//2

            if m == len(matrix)-1:
                if matrix[m][0] <= target:
                    ind = len(matrix)-1
                    break
                else:
                    ind = len(matrix)-2
                    break
            else:
                if matrix[m][0] > target:
                    r = m-1
                elif matrix[m][0] <= target and matrix[m+1][0] > target:
                    ind = m
                    break
                else:
                    l = m+1
        

        arr = matrix[ind]

        l = 0
        r = len(arr)-1
        print(ind)

        while l <= r:

            m = (l+r)//2

            if arr[m] < target:
                l = m+1
            elif arr[m] > target:
                r = m-1
            else:
                return True
        
        return False

        