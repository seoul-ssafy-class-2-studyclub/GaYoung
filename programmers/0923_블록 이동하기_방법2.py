board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

n = len(board)
visit = [[[0] * n for _ in range(n)] for _ in range(2)]
# 로봇이 가로, 세로인 경우를 하나하나 표시하면서 가기!
# 내가 기존에 했던 방법이랑 동일

for i in range(n):
    for j in range(n):
        visit[i][j] = 0