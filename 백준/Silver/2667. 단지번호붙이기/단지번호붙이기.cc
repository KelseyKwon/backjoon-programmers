// // 좌우, 아래위로 있으면 연결됨.
// // 만약에 상하좌우가 1이면 -> count++하고 그 곳으로 가서 상화좌우가 1...
// // dfs로 계속 부름

// #include <iostream>
// #include <vector>

// using namespace std;

// int N, count;
// vector<vector<int>> graph;
// vector<vector<bool>> visited;

// int dx[] = {0, 1, 0, -1};
// int dy[] = {1, 0, -1, 0};

// int dfs(int start, int end) {
//   for (int i=start; i<N; i++) {
//     for (int j=end; j<N; j++) {
//       if (graph[i][j] == 1) {
//         count++;
//         visited[i][j] = true;
//         for (int i=0; i<4; i++) {
//           int ni = i + dx[i];
//           int nj = j + dx[j];

//           if (graph[ni][nj] == 1 && !visited[ni][nj]) {
//             dfs(ni, nj);
//           }
//         }
//       }
//     }
//   }
// }

// int main() {
//   cin >> N;
//   graph.resize(N, vector<int>(N));
//   visited.resize(N, vector<bool>(N, false));
//   vector<int> house_count;

//   for (int i=0; i<N; i++) {
//     for (int j=0; j<N; j++) {
//       cin >> graph[i][j];
//     }
//   }

//   for (int i=0; i<N; i++) {
//     for (int j=0; j<N; j++) {
//       count = 0;
//       if (!visited[i][j] &&graph[i][j] == 1) {
//         house_count.push_back(dfs(i, j));
//       }
//     }
//   }

// }

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int N;
vector<vector<int>> graph;
vector<vector<bool>> visited;

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

int dfs(int x, int y) {
    visited[x][y] = true;
    int cnt = 1;

    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
            if (graph[nx][ny] == 1 && !visited[nx][ny]) {
                cnt += dfs(nx, ny);
            }
        }
    }
    return cnt;
}

int main() {
    cin >> N;
    graph.resize(N, vector<int>(N));
    visited.resize(N, vector<bool>(N, false));

    // for (int i=0; i<N; i++) {
    //     for (int j=0; j<N; j++) {
    //         cin >> graph[i][j];
    //     }
    // }
    for (int i=0; i<N; i++) {
      string s;
      cin >> s;
      for (int j=0; j<s.size(); j++) {
        graph[i][j] = s[j] - '0'; // char -> int 변환
      }
    }

    vector<int> house_count;

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (!visited[i][j] && graph[i][j] == 1) {
                house_count.push_back(dfs(i, j));
            }
        }
    }

    sort(house_count.begin(), house_count.end());

    cout << house_count.size() << '\n';
    for (int h : house_count) cout << h << '\n';
}


    cout << house_count.size() << '\n';
    for (int h : house_count) cout << h << '\n';
}
