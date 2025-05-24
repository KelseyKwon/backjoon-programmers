#include <bits/stdc++.h>

using namespace std;

int N, M;
vector<vector<int>> graph;
vector<vector<bool>> visited;


int dy[] = {1, 0, -1, 0};
int dx[] = {0, 1, 0, -1};

bool inRange(int y, int x) {
    return (y >= 1 && y <= N && x >= 1 && x <= M);
}

int bfs(int y, int x) {
    // 안 방문했고, 범위 안에 있고, 1이면.
    // priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>, greater<>>> pq;
    // 
    queue<tuple<int, int, int>> q;
    q.push({1, y, x});
    visited[y][x] = true;

    while(!q.empty()) {
        int cost, cur_y, cur_x;
        tie(cost, cur_y, cur_x) = q.front(); q.pop();

        if (cur_y == N && cur_x == M) {
            return cost;
        }

        for (int i=0; i<4; i++) {
            int ny = cur_y + dy[i];
            int nx = cur_x + dx[i];

            // if (!visited[ny][nx] && inRange(ny, nx) && graph[ny][nx]) {
            if (inRange(ny, nx) && !visited[ny][nx] && graph[ny][nx]) {
                visited[ny][nx] = true;
                q.emplace(cost+1, ny, nx);
            }
        }
    }
    return -1; //반드시 적기 ! 도달할 수 없는 경우.
}

int main() {
    cin >> N >> M;
    graph.resize(N+1, vector<int>(M+1));
    visited.resize(N+1, vector<bool>(M+1, false));

    for (int i=1; i<=N; i++) {
        string s;
        cin >> s;
        for (int j=1; j<=s.size(); j++) {
            // graph[i][j] = s[j] - '0';
            graph[i][j] = s[j-1] - '0';
        }
    }

    int answer = bfs(1, 1);
    cout << answer;
}