board = [[0] * 100 for _ in range(100)]
cnt_ans = 0
for t in range(4):
    cnt = 0
    r1, c1, r2, c2 = map(int, input().split())
    for i in range(r1, r2):
        for j in range(c1, c2):
            board[i][j] += 1
            cnt += 1

for k in range(100):
    for l in range(100):
        if board[k][l] >= 1:
            cnt_ans += 1
print(cnt_ans)
