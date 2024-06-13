'''
1.아이디어
- 2중 for문 값 1 && 방문x -> dfs
- dfs를 통해 찾은 값을 저장 후 정렬해서 출력

2.시간복잡도
- dfs : o(v + e)
- v, e : n^2 , n^2 * 4
- v + e : 5n^2 == n^2 == 625 >> 가능

3. 자료구조
- 그래프 저장 : int[][]
- 방문여부 : bool[][]
- 결과값 : int[]

입력
첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

출력
첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

'''

import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int, input().strip())) for _ in range(n)]
chk = [[False] * n for _ in range(n)]
result = []
each = 0

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global each # 전역변수로 변경
    each += 1 
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0 <= nx <n:
            if map[ny][nx] == 1 and chk[ny][nx] == False:
                chk[ny][nx] = True
                dfs(ny, nx)
                
for j in range(n):
    for i in range(n):
        if map[j][i] == 1 and chk[j][i] == False:
            # 방문 체크 표시
            chk[j][i] = True
            # dfs로 크기 구하기 
            # 크기를 결과 리스트에 넣기
            each = 0 
            dfs(j, i)
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)