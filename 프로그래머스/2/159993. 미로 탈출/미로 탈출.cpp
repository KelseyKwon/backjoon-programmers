// S -> L, L -> E로 가야함. 
// 최소시간 -> 탐색... 그래프...  bfs!

#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;
int n, m;

int dx[] = {0, -1, 0, 1};
int dy[] = {1, 0, -1, 0};

// pair로 하는 것은 직관적이지 않다. 따로 구조체를 만들어서 하는게 더 좋음!
struct Point {
    int y, x, cnt;
};

Point find_start_point(vector<string> &maps, char where) {
    for (int i=0; i<n; i++) {
        for (int j=0; j<m; j++) {
            if (maps[i][j] == where) {
                return {i, j, 0};
            }
        }
    }
    return {-1, -1, -1};
}

bool isWithInRange(int y, int x) {
    return (y < n && y >= 0 && x < m && x >=0);
}

int bfs(vector<string> &maps, char start, char end) {
    queue<Point> heap;
    // 초기화하는법법
    bool visited[101][101] = {false};
    
    Point S = find_start_point(maps, start);
    visited[S.y][S.x] = true;
    heap.push(S);

    while (!heap.empty()) {
        Point cur_point = heap.front();
        // visited[cur_point.y][cur_point.x] = true;
        heap.pop();

        if (maps[cur_point.y][cur_point.x] == end) {
            return cur_point.cnt;
        }

        for (int i=0; i<4; i++) {
            int next_y = cur_point.y + dy[i];
            int next_x = cur_point.x + dx[i];

            if (isWithInRange(next_y, next_x) && !visited[next_y][next_x] && maps[next_y][next_x] != 'X') {
                heap.push({next_y, next_x, cur_point.cnt+1});
                visited[next_y][next_x] = true;
            }
        }
    }
    return -1;
    
}

int solution(vector<string> maps) {
    n = maps.size();
    m = maps[0].size();

    // 일단 그래프를 순회하고, 상하좌우중에 O이면 가고, L이면 탈출.
    // start가 다를 수 있다. start의 좌표를 찾아야 함.
    
    int distance_to_L = bfs(maps, 'S', 'L');
    if (distance_to_L == -1) {
        return -1;
    }

    int distance_to_E = bfs(maps, 'L', 'E');
    if (distance_to_E == -1) {
        return -1;
    }
    return distance_to_L + distance_to_E;
}