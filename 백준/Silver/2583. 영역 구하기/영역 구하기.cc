/*
일단 5행, 7열, 3개

M : y, N : x
0,0 -> 4,0            7,5 -> 
0,2 -> 3,3
4,0 -> 5,1

x, y->x-1, y-1
일단 숫자를 입력 받아 -> 0~3, 2~3까지 1로 칠해 -> 반복해

그다음에 dfs해(해당 칸이 0이면) -> 돌아오면 count를 해. 
각 영역의 넓이를 오름차순으로 정렬하고 출력해. 

4,0 -> 0,0
*/
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
vector<vector<int>> graph;
vector<vector<bool>> visited;

int M, N, K;
//기존 x + 바뀐 x = 4 4-기존x.
// 0,0 -> 4,0 
// 1,0 -> 3,0
// 2,0 -> 2,0
// 3,0 -> 1,0
// 4,0 -> 0,0
int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

bool inRange(int y, int x) {
  return (y >= 0 && y < M && x >= 0 && x < N);
}

int dfs(int y, int x, int count) {
  visited[y][x] = true;
  for (int i=0; i<4; i++) {
    int nx = x + dx[i];
    int ny = y + dy[i];

    if (inRange(ny, nx) && !visited[ny][nx] && graph[ny][nx] == 0) {
      // dfs(ny, nx, count++);
      count = dfs(ny, nx, count+1);
    }
  }
  return count;
}

void draw(int y1, int x1, int y2, int x2) {
  for (int i=y1; i<y2; i++) {
    for (int j=x1; j<x2; j++) {
      if (graph[i][j] == 1) continue;
      graph[i][j] = 1;
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> M >> N >> K;
  graph.assign(M, vector<int>(N, 0));
  visited.assign(M, vector<bool>(N, false));

  for (int i=0; i<K; i++) {
    int y1, x1, y2, x2;
    cin >> x1 >> y1 >> x2 >> y2;
    draw(M-y2, x1, M-y1, x2);
  }

  vector<int> answer;

  for (int i=0; i<M; i++) {
    for (int j=0; j<N; j++) {
      int count = 1;
      if (!visited[i][j] && graph[i][j] == 0) {
        answer.push_back(dfs(i, j, count));
      }
    }
  }
  sort(answer.begin(), answer.end());
  cout << answer.size() << endl;
  for (int i : answer) {
    cout << i << " ";
  }

  return 0;
}