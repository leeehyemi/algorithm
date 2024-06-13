'''
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

bfs , queue 이용
2중 for문 -> 1, 방문하지 않은 곳만 bfs

1. 아이디어 
: 2중 for문 -> 1 && 방문x -> bfs
bfs 돌면서 그림 개수 +1, 최대값 갱신

2. 시간복잡도 
- bfs o(e + v) = v + e = v + 4v = 5v
-> 5 (mxn) = 5 x (500 * 500) = 100만  < 2억개 가능
- v : m x n 
- e : v x 4

3.자료구조
- 그래프 전체 지도 : int [][]
- 방문 : bool[][]
- Queue(BFS)
'''

import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

cnt = 0
maxv = 0
dy = [0, 1, 0, -1] # 오른쪽 왼쪽
dx = [1, 0, -1, 0] # 아래쪽 위쪽

def bfs(y, x):
    rs = 1 # 그림의 사이즈 
    q = deque()
    q.append((y,x))
    while q:
        ey, ex = q.popleft()
        for k in range(4):
           ny = ey + dy[k]
           nx = ex + dx[k]
           if 0 <= ny < n and 0 <= nx < m:
               if map[ny][nx] == 1 and chk[ny][nx] == False:
                   rs += 1
                   chk[ny][nx] = True
                   q.append((ny, nx))
    return rs

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            # 전체 그림 개수 +1
            cnt += 1
            # bfs를 통해서 그림 크기를 구해줌
            # 최대값 갱신
            maxv = max(maxv, bfs(j,i))

print(cnt)
print(maxv)