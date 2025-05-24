/*
1, 2 (가로) -> 가로로 갔는데 끝이 열이나 행 끝에 있고, 끝점이 도착점이 아니야. 그러면 백트래킹
1, 2 -> 2, 2 ok.
2, 2-> 3, 3 (나머지는 행 or 열 끝.)

1, 2 -> 1, 3 (1, 4)안됨 -> 2, 4 대각선은 열의 끝이거나 행의 끝이여도 됨. 

대각선 : 행+1, 열+1, (행+1, 열+1)
가로 : (행+1, 열+1), 열+1
세로 : (행+1, 열+1), 행+1. 

일단 next 좌표들을 구한다음에, 벽이 아니고, 범위를 안벗어나면 계속 -> 근데 끝점이면 break!
*/

/*
#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> graph;

struct Period {
    int y, x;
    char dir;
};



int main() {
    int N;
    cin >> N;
    
    graph.resize(N+1);

    queue<Period> cur;

    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            cin >> graph[i][j];
        }
    }

    cur.push({1, 2, 'A'});

    while(cur.front().y <N && cur.front().x <N) {
        int cur_x, cur_y; char cur_dir;
        // tie(cur_y, cur_x, cur_dir) = cur.front();
        auto [cur_y, cur_x, cur_dir] = cur.front(); 

        if (cur_dir = 'A') {

        }

        if (cur_dir = 'B') {

        }

        if (cur_dir = 'C') {

        }
    }

    return 0;
}
    */


#include <bits/stdc++.h>

using namespace std;

// 2차원 배열의 인덱스 값이 적게 정의되면 미리 이렇게 정의하는게 더 나음.
bool maps[17][17];
int N;
int answer = 0;

int dy[] = {1, 0, 1};
int dx[] = {0, 1, 1};

bool check(int y, int x) {
    return (y > N || y < 1 || x > N || x < 1 || maps[y][x] == 1);
}

void dfs(int y, int x, int dir) {
    if (y == N && x == N) {answer++; return;}
    for (int i=0; i<3; i++) {
        // 가로 -> 세로, 세로 -> 가로 안됨.
        if ((dir == 0 && i == 0) || (dir == 1 && i == 1)) continue;
        int ny = y + dy[i];
        int nx = x + dx[i];
        // if(check(ny, nx)) continue;

        // // 대각선인데 나머지 칸이 벽이면면
        // // if (dir == 2 && (maps[y][x+1] == 1 || maps[y+1][x] == 1)) continue;
        // if (i == 2 && (maps[y][x + 1] || maps[y + 1][x] || maps[y + 1][x + 1])) continue;
        // dfs(ny, nx, i);
        if (i == 2) {
    if (check(ny, nx) || maps[y][x + 1] || maps[y + 1][x]) continue;
} else {
    if (check(ny, nx)) continue;
}
dfs(ny, nx, i);
    }

}

int main() {
    cin >> N;

    for (int i=1; i<=N; i++) {
        for (int j=1; j<=N; j++) {
            cin >> maps[i][j];
        }
    }

    dfs(1, 2, 0);
    cout << answer;

    return 0;
}
