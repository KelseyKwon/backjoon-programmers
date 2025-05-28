/*
1초

M, N, K가 1!

graph에 저장.
상하좌우. !viisted & 배열 범위 내 & 상하좌우가 1이면 -> 글로가
그리고 return +1;

오류 ; dfs임...

*/
#include <iostream>
#include <vector>

using namespace std;

int M, N, K;
vector<vector<int>> graph;
vector<vector<bool>> visited;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

bool inRange(int x, int y) {
  return (x >=0 && x < N && y >= 0 && y < M);
}

// 이제 1인 곳부터 시작을 해
void dfs(int x, int y) {
  visited[x][y] = true;

  for (int i=0; i<4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];

//    if (!visited[nx][ny] && inRange(nx, ny) && graph[nx][ny]) {
      if (inRange(nx, ny) && !visited[nx][ny] && graph[nx][ny]==1) {
      dfs(nx, ny);
    }
  }
}

int main() {
   ios::sync_with_stdio(false);
  cin.tie(NULL); 
   
  int T;
  cin >> T;

  for (int i=0; i<T; i++) {
    cin >> M >> N >> K;
    graph.assign(N, vector<int>(M));
    visited.assign(N, vector<bool>(M, false));

    for (int i=0; i<K; i++) {
      int u, v;
      cin >> u >> v;
      graph[v][u] = 1;
    }

    int answer = 0;
  for (int i=0; i<N; i++) {
    for (int j=0; j<M; j++) {
      if (!visited[i][j] && graph[i][j] == 1) {
        dfs(i, j);
        answer++;
      }
    }
  }
  cout << answer << endl;
  }
}
