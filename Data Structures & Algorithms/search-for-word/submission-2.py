class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_rows, num_cols = len(board), len(board[0])

        def dfs(row, col, idx):
            if idx == len(word):
                return True

            invalid_cell = (
                row < 0 or
                col < 0 or
                row >= num_rows or
                col >= num_cols or
                board[row][col] == "#" or
                board[row][col] != word[idx]
            )
            if invalid_cell:
                return False

            directions = (
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1)
            )
            
            original_char = board[row][col]
            board[row][col] = "#"
            for direction in directions:
                if dfs(direction[0], direction[1], idx + 1):
                    return True
            
            board[row][col] = original_char


        for row in range(num_rows):
            for col in range(num_cols):
                if dfs(row, col, 0):
                    return True
        return False