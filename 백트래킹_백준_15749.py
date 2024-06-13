"""
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

    1. 아이디어
    - 백트래킹 재귀함수 안에서, for 돌면서 숫자 선택(이때 방문여부 확인)
    - 재귀함수에서 m개를 선택할 경우 print
    
    2. 시간복잡도
    - n! > 가능 (중복 불가능한 경우)(가능하면 n제곱) 
    
    3. 자료구조
    - 결과값 저장 int[]
    - 방문여부 체크 bool[]
    
    백트래킹은 n이 작음 (10이하)
    백트래킹은 종료시점 꼭 기재해야함
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rs = []
chk = [False] * (n+1) # 1부터 사용함

def requr(num):
    if num == m:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, n+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(i)
            requr(num+1)
            chk[i] = False
            rs.pop()
        
requr(0)