class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in board:
            if not self.isValid9(i):
                print("Failed at the horizontal board")
                return False
        
        for j in range(9):
            val = []

            for i in board:
                val.append(i[j])

            if not self.isValid9(val):
                print("Failed at the vertical board")
                return False
        
        for i in range(0,7,3):
            for j in range(0,7,3):
                val = []

                for k in range(i,i+3):
                    for l in range(j,j+3):
                        val.append(board[k][l])

                if not self.isValid9(val):
                    print("Failed at the square")
                    return False

        return True

    def isValid9(self, board: List[str]) -> bool:
        occ = {}

        for i in board:

            if i == '.':
                continue
            if i in occ:
                return False
            occ[i] = True

        return True
        