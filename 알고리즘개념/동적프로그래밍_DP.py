'''
[ 동적프로그래밍 개념 ]
    1. 해결된 문제의 답을 저장해두고 그것을 재활용하여 해결된 문제를 다시 푸는 비효율을 제거
    2. 공간복잡도를 늘리고 시간복잡도를 줄이는 방식
'''

'''
[DP 사용 경우]
 - 최적 부분문제 구조(Optimal substructure)
 - 중복 부분문제 구조(Overlapping subproblems)

[ 3단계 DP 적용 접근 방법 ]
  1. 최적해 구조의 특성을 파악하라
     - 문제를 부분 문제로 나눈다.
  2. 최적해의 값을 재귀적으로 정의하라
     - 부분 문제의 최적해 값에 기반하여 문제의 최적해 값을 정의한다.
  3. 상향식 방법으로 최적해의 값을 계산하라
     - 가장 작은 부분 문제부터 해를 구한 뒤 테이블에 저장한다.
     - 테이블에 저장되어 있는 부분 문제의 해를 이용하여 점차적으로 상위 부분 문제의 최적해를 구한다. (상향식 방법)
'''


# 예제1. 피보나치 수 DP 적용
def fibo(n):
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f
print(fibo(10))


# 예제2. 1로 만들기 -> 백준 1463
