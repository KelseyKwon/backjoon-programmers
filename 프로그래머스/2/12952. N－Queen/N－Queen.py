"""
그 전에 선택을 안했고, 현재에서 대각선상에 위치하지 않은 것을 선택한다. 
"""

def solution(n):
    
    def backtrack(board, row, n):
        count = 0
        if n == row:
            return 1
        # row 행에서 가능한 모든 열을 시도한다
        for col in range(n):
            # row 행에 col열에 퀸을 둔다. 
            board[row] = col
            for i in range(row):
                # 같은 열 충돌
                if board[i] == board[row]:
                    break
                    # 대각선 충돌 -> 행 차이와 열 차이가 같으면 대각선 충돌.
                if abs(board[i] - board[row]) == row - i:
                    break
            else:
                count += backtrack(board, row+1, n)
        return count
    return backtrack([0] * n , 0, n)