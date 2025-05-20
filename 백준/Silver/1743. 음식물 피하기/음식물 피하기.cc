#include <bits/stdc++.h>
using namespace std;

int N, M, K;
vector<vector<bool>> grid, visited;
int dx[4] = {-1,0,1,0}, dy[4] = {0,-1,0,1};

bool inRange(int x, int y) {
    return x>=0 && x<N && y>=0 && y<M;
}

// (x,y)에서 시작한 연결 요소 크기를 리턴
int dfs(int x, int y) {
    visited[x][y] = true;
    int cnt = 1;
    for (int d = 0; d < 4; d++) {
        int nx = x + dx[d];
        int ny = y + dy[d];
        if (inRange(nx, ny)
            && !visited[nx][ny]
            && grid[nx][ny]
        ) {
            cnt += dfs(nx, ny);
        }
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M >> K;
    grid.assign(N, vector<bool>(M, false));
    visited.assign(N, vector<bool>(M, false));

    for (int i = 0; i < K; i++) {
        int r, c;
        cin >> r >> c;
        r--; c--;                  // 1-based → 0-based
        grid[r][c] = true;
    }

    int answer = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (grid[i][j] && !visited[i][j]) {
                answer = max(answer, dfs(i, j));
            }
        }
    }

    cout << answer;
    return 0;
}
