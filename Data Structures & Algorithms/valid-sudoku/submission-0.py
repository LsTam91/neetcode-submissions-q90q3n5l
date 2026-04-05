class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in col[i] or board[i][j] in row[j] or board[i][j] in square[(i//3,j//3)]:
                    return False
                col[i].add(board[i][j])
                row[j].add(board[i][j])
                square[(i//3,j//3)].add(board[i][j])
        return True