'''
[풀이방법]
1. turn 함수 생성 -> (3,4,2), (4,2,1)연산 수행
2. mymin 지정해서 연산 수행이 끝날 때마다 최소값 구하기
  2-1. (3,4,2), (4,2,1)연산 수행 하면서 mymin 갱신
  2-2. (4,2,1), (3,4,2)연산 수행 하면서 mymin 갱신

'''

import itertools

def turn(r, c, s):









N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
do_ls = [list(map(int, input().split())) for _ in range(K)]

results = list(itertools.permutations(do_ls, K))
# print(result)  # [([3, 4, 2], [4, 2, 1]), ([4, 2, 1], [3, 4, 2])]

mymin = 9999999999999999999
for result in results:
    row_sum = 0
    for r, c, s in result:
        turn(r, c, s)





    if mymin > row_sum:
        mymin = row_sum

print(mymin)