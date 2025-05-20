/*
// 세로 길이 N, 가로 길이 M, 음식물 쓰레기 개수 K
// 

// vector<pair<int, int>> 로 저장하고
// 상하좌우 확인해서 있으면 -> dfs 아니면 ... 

#include <iostream>
#include <vector>
#include <algorithm>   // for std::find

using namespace std;

int N, M, K;
vector<bool> visited;
vector<pair<int, int>> trash;
int dx[] = {-1, 0, 1, 0};
int dy[] = {0, -1, 0, 1};

bool isInRightRange(int x, int y) {
    return (x >= 0 && x < N && y >= 0 && y < M);
}

int dfs(int x, int y, int size) {
    visited[x+y-1] = true;

    for (int i=0; i<4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (!visited[nx+ny-1] &&
            isInRightRange(nx, ny) &&
            find(trash.begin(), trash.end(), make_pair(nx, ny)) != trash.end()) {
                dfs(nx, ny, size++);
            }
    }
    return size;
}

int main() {
    cin >> N >> M >> K;
    visited.resize(N*M, false);

    for (int i=0; i<K; i++) {
        int x, y;
        cin >> x >> y;

        trash.push_back({x, y});
    }

    int answer = 0;
    for (int i=0; i<trash.size(); i++) {
        int cur_max_size = dfs(trash[i].first, trash[i].second, 1);
        answer = max(answer, cur_max_size);
    }
    cout << answer;

}
*/

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

